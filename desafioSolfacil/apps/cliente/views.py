from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from .serializers import ClienteSerializer, ImportCSVSerializer
from .models import ClienteModel
import csv
from io import TextIOWrapper
import requests


class ClienteViewSet(ModelViewSet):
    serializer_class = ClienteSerializer
    queryset = ClienteModel.objects.all()
    http_method_names = ["options", "get", "post", "patch", "put", "delete"]

    @swagger_auto_schema(
        operation_description="Upload a CSV file.",
        request_body=ImportCSVSerializer,
    )
    @action(methods=['post'], detail=False, parser_classes=(FormParser, MultiPartParser, FileUploadParser))
    def import_csv(self, request, *args, **kwargs):
        file = request.FILES['file']
        file_extension = file.name.split('.')[-1] if '.' in file.name else None

        if file_extension == 'csv':
            validados = []
            invalidados = []
            text_csv_file = TextIOWrapper(file.file, encoding='utf-8-sig')

            reader = csv.reader(text_csv_file)
            next(reader)
            for row in reader:
                try:
                    cliente = self.__validateRow(row)
                    if cliente is not None:
                        validados.append(row[0])
                    else:
                        invalidados.append(row[0])
                except Exception:
                    invalidados.append(row[0])

            data = {
                'validados': validados,
                'invalidados': invalidados,
            }
            return Response(data=data, status=200)
        else:
            return Response('Apenas arquivos CSV são permitidos', status=400)

    def __validateRow(self, row):
        try:
            if row[0] is not None:
                cliente = self.__getClient(row)
                if cliente is not None:
                    return self.__update_client(row, cliente)
                else:
                    if len(row[0]) == 14:
                        return self.__create_client_cpf(row)

                    elif len(row[0]) == 18:
                        return self.__create_client_cnpj(row)

                    else:
                        return None
            else:
                return None
        except Exception:
            return None

    def __getClient(self, row):
        cliente = ClienteModel.objects.filter(cnpj=row[0])
        if len(cliente) > 0:
            return cliente.first()
        else:
            cliente = ClienteModel.objects.filter(cpf=row[0])
            if len(cliente) > 0:
                return cliente.first()
            else:
                return None

    def __update_client(self, row, cliente):
        cep, cidade, estado = self.__consultaCep(row[5])

        if cep is not None:
            cliente.razao_social = row[1]
            cliente.nome_fantasia = row[2]
            cliente.telefone = row[3]
            cliente.email = row[4]
            cliente.cidade = cidade
            cliente.estado = estado
            cliente.cep = cep
            cliente.save()
            return cliente
        else:
            return None

    def __create_client_cpf(self, row):
        cep, cidade, estado = self.__consultaCep(row[5])

        if cep is not None:
            cliente = ClienteModel(
                cpf=row[0],
                razao_social=row[1],
                nome_fantasia=row[2],
                telefone=row[3],
                email=row[4],
                cidade=cidade,
                estado=estado,
                cep=cep
            )

            cliente.save()
            return cliente

        else:
            return None

    def __create_client_cnpj(self, row):
        cep, cidade, estado = self.__consultaCep(row[5])

        if cep is not None:
            cliente = ClienteModel(
                cnpj=row[0],
                razao_social=row[1],
                nome_fantasia=row[2],
                telefone=row[3],
                email=row[4],
                cidade=cidade,
                estado=estado,
                cep=cep
            )

            cliente.save()
            return cliente
        else:
            return None

    def __consultaCep(self, cep):
        response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        if response.status_code == 200:
            endereco = response.json()
            return cep, endereco['localidade'], endereco['uf']
        else:
            return None
