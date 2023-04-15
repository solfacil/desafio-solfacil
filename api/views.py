from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models import Parceiro
from api.repository import ParceiroRepository
from api.serializers import ParceiroSerializer
from api.utils import process_and_save_csv_values, validate_fields_partner


class ParceiroViewSet(viewsets.ModelViewSet):
    queryset = Parceiro.objects.all().order_by("id")
    serializer_class = ParceiroSerializer
    permission_classes = (IsAuthenticated,)
    http_method_names = ["get", "post", "put", "delete"]

    def list(self, request, *args, **kwargs):
        return super().list(request, args, kwargs)

    def create(self, request, *args, **kwargs):
        try:
            validate_fields_partner(request.data)

            ParceiroRepository.save_partner(request.data)

            return Response(
                "Parceiro salvo/atualizado com sucesso!", status=status.HTTP_201_CREATED
            )

        except Exception as error:
            return Response(
                f"Houve um problema ao salvar o parceiro por: {error}",
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def update(self, request, *args, **kwargs):       
        try:
            partner = Parceiro.objects.filter(cnpj=request.data["cnpj"]).first()
            if not partner:
                return Response(
                    {"error": "Parceiro não encontrado"},
                    status=status.HTTP_404_NOT_FOUND,
                )
            validate_error = validate_fields_partner(request.data)
            if validate_error:
                return Response(
                    {"errors": validate_error}, status=status.HTTP_400_BAD_REQUEST
                )

            ParceiroRepository.save_partner(request.data)

            return Response(
                "Parceiro atualizado com sucesso!", status=status.HTTP_200_OK
            )

        except Exception as error:
            return Response(
                f"Houve um problema ao salvar o parceiro por {error}",
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

  
    @action(detail=False, methods=["post"], url_path="csv-upload")
    def csv_upload(self, request):
        """
            Essa função recebe um determinado arquivo csv e faz a leitura dos dados
        """
        csv_file = request.FILES.get("csv_file")
        if csv_file:
            parceiro_repository = ParceiroRepository()
            try:
                process_and_save_csv_values(csv_file, parceiro_repository)
            except Exception as e:
                return Response(
                    {
                        "error": f"existem valores errados no CSV, verifique os campos: {e} os objetos do CSV que estiverem sem problema, foram salvos"
                    },
                    status=status.HTTP_207_MULTI_STATUS,
                )
            else:
                return Response(
                    {"success": "Parceiros cadastrados com sucesso"},
                    status=status.HTTP_200_OK,
                )
        else:
            return Response(
                {"error": "Nome do csv incorreto ou tipo de arquivo errado."},
                status=status.HTTP_400_BAD_REQUEST,
            )
