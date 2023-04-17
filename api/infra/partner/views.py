import csv
from io import StringIO
from typing import List

from django.db import transaction
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.response import Response

from api.application.partner.partner_dto import PartnerDto
from api.application.partner.partner_manager import PartnerManager
from api.presenters.helpers import server_error

from .models import Partner
from .repositories import PartnerRepository
from .serializers import PartnerSerializer
from .utils import PartnerAddressApi


class PartnerViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    __partner_manager = PartnerManager(PartnerRepository(), PartnerAddressApi())

    def list(self, request, *args, **kwargs):
        http_response = self.__partner_manager.get_all_partners()
        return Response(
            PartnerSerializer(http_response["body"], many=True).data,
            status=http_response["status_code"],
        )

    def create(self, request, *args, **kwargs):
        raise MethodNotAllowed("POST")

    def retrieve(self, request, *args, **kwargs):
        raise MethodNotAllowed("GET")

    def update(self, request, *args, **kwargs):
        raise MethodNotAllowed("PUT")

    def partial_update(self, request, *args, **kwargs):
        raise MethodNotAllowed("PUT")

    def destroy(self, request, *args, **kwargs):
        raise MethodNotAllowed("DELETE")

    @action(detail=False, methods=["post"], url_path="upload")
    def upload(self, request) -> Response:
        try:
            file = request.FILES.get("file")
            with StringIO(file.read().decode("utf-8")) as temp:
                partners_dto: List[PartnerDto] = []
                for data in csv.DictReader(temp):
                    partners_dto.append(
                        PartnerDto(
                            id=None,
                            cnpj=data["CNPJ"]
                            .replace(".", "")
                            .replace("/", "")
                            .replace("-", ""),
                            cpf=None,
                            corporate_name=data["Razão Social"],
                            trading_name=data["Nome Fantasia"] or None,
                            phone=data["Telefone"]
                            .replace("(", "")
                            .replace(")", "")
                            .replace("-", "")
                            .replace(" ", "")
                            or None,
                            email=data["Email"],
                            cep=data[" CEP"].replace("-", ""),
                            uf=None,
                            city=None,
                        )
                    )

                with transaction.atomic():
                    http_response = self.__partner_manager.create_or_update_partners(
                        partners_dto
                    )
                    if http_response["status_code"] > 299:
                        transaction.set_rollback(True)
                    return Response(
                        http_response["body"]
                        if http_response["status_code"] >= 200
                        and http_response["status_code"] <= 299
                        else {"error": str(http_response["body"])},
                        status=http_response["status_code"],
                    )
        except Exception as e:
            print(e)
            http_response = server_error()
            return Response(
                {"error": str(http_response["body"])},
                status=http_response["status_code"],
            )
