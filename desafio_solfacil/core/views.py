from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from desafio_solfacil.core.models import Parceiro
from desafio_solfacil.core.serializers import (
    ParceiroImportSerializer,
    ParceiroSerializer,
)


# Create your views here.


class ParceiroView(ModelViewSet):
    queryset = Parceiro.objects.all()
    serializer_class = ParceiroSerializer

    @swagger_auto_schema(
        request_body=ParceiroImportSerializer,
    )
    @action(
        detail=False,
        methods=["post"],
        url_path="import",
        url_name="import_parceiros",
    )
    def import_parceiros(self, request):
        serializer = ParceiroImportSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = {}
        if serializer.validated_data["errors"]:
            data.update(
                {
                    "mensagem": "Foram encontrados erros na importação",
                    "errors": serializer.validated_data["errors"],
                }
            )

        data.update(
            {
                "data": serializer.validated_data["instances"],
            }
        )

        return Response(data, status=status.HTTP_201_CREATED)

    def get_serializer_class(self):
        if self.action == "import_parceiros":
            return ParceiroImportSerializer
        return super().get_serializer_class()
