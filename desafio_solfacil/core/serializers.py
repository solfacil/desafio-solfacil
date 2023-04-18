import re

import pandas as pd

from rest_framework import serializers

from desafio_solfacil.core.models import Parceiro
from services.viacep_api import ViaCepApi


class ParceiroSerializer(serializers.ModelSerializer):
    def update_endereco_by_cep(self, instance, validated_data):
        if (
            "cep" in validated_data
            and validated_data["cep"] != self.initial_data["cep"]
        ):
            cep = validated_data["cep"]
            endereco = ViaCepApi().get_address(cep)
            if endereco:
                instance.endereco = endereco["logradouro"]
                instance.cidade = endereco["localidade"]
                instance.estado = endereco["uf"]

    def validate(self, attrs):
        if "cnpj" in attrs:
            attrs["cnpj"] = re.sub(r"[^0-9]", "", attrs["cnpj"])
        if "cep" in attrs:
            attrs["cep"] = re.sub(r"[^0-9]", "", attrs["cep"])
        return attrs

    def create(self, validated_data):
        instance = super().create(validated_data)
        self.update_endereco_by_cep(instance, validated_data)
        return instance

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        self.update_endereco_by_cep(instance, validated_data)
        return instance

    class Meta:
        model = Parceiro
        fields = "__all__"
        read_only_fields = ("cidade", "estado", "endereco")


class ParceiroImportSerializer(serializers.Serializer):
    # Aceitar apenas arquivos CSV
    data = serializers.FileField(allow_empty_file=False)

    def validate(self, attrs):
        # Validar se o arquivo é CSV
        if attrs["data"].name.split(".")[-1] != "csv":
            raise serializers.ValidationError("Arquivo inválido")

        data = pd.read_csv(attrs["data"])
        instances = []
        errors = []

        data.columns = [
            self.normalize_column_name(col) for col in data.columns
        ]

        for index, row in data.iterrows():
            try:
                instance, data, created = self.create_update_instance(row)
                instances.append(data)
                if created:
                    instance.enviar_email_boas_vindas()
            except serializers.ValidationError as e:
                errors.append(
                    {
                        "linha": index + 2,
                        "mensagem": e.detail,
                    }
                )

        attrs["instances"] = instances
        attrs["errors"] = errors
        return attrs

    @staticmethod
    def create_update_instance(data):
        data.where(pd.notnull(data), None, inplace=True)
        created = False
        try:
            instance = Parceiro.objects.get(
                cnpj=re.sub(r"[^0-9]", "", data["cnpj"])
            )
            serializer_kwargs = {"instance": instance}
        except Parceiro.DoesNotExist:
            created = True
            serializer_kwargs = {}

        serializer_kwargs.update(
            {
                "data": {
                    "cnpj": data["cnpj"],
                    "razao_social": data.get("razão_social", None),
                    "nome_fantasia": data.get("nome_fantasia", None),
                    "telefone": data.get("telefone", None),
                    "email": data.get("email", None),
                    "cep": data.get("cep", None),
                }
            }
        )

        serializer = ParceiroSerializer(**serializer_kwargs)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return serializer.instance, serializer.data, created

    @staticmethod
    def normalize_column_name(value):
        value = value.lower()
        if value.startswith(" "):
            value = value[1:]
        if value.endswith(" "):
            value = value[:-1]

        return value.replace(" ", "_")
