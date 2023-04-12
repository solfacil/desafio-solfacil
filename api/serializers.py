from rest_framework import serializers

from api.models import Endereco, Parceiro


class ParceiroSerializer(serializers.ModelSerializer):


    class Meta:
        model = Parceiro
        fields = '__all__'

class EnderecoSerializer(serializers.ModelSerializer):


    class Meta:
        model = Endereco
        fields = '__all__'