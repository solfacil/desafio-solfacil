import unittest
from typing import List

from api.application.partner.address_api import AddressApi
from api.application.partner.partner_dto import PartnerDto
from api.application.partner.partner_manager import PartnerManager
from api.application.partner.partner_storage import PartnerStorage
from api.presenters.helpers.http_helper import bad_request, created, ok, server_error


class DummyAddressApi(AddressApi):
    def handle(self, cep: str):
        return {"uf": "valid_uf", "city": "valid_city"}


class DummyStorage(PartnerStorage):
    partner_dto: PartnerDto

    def __init__(self) -> None:
        self.partner_dto = PartnerDto(
            id="valid_id",
            cnpj="valid_cnpj",
            cpf="valid_cpf",
            corporate_name="valid_corporate_name",
            trading_name="valid_trading_name",
            phone="valid_phone",
            email="valid_email",
            cep="valid_cep",
            uf="valid_uf",
            city="valid_city",
        )

    def save_or_update_partner(self, partner_dto: PartnerDto):
        self.partner_dto = partner_dto
        return True

    def get_all_partners(self) -> List[PartnerDto]:
        return [self.partner_dto]


class PartnerManagerTests(unittest.TestCase):
    def setUp(self):
        self.dummy_storage = DummyStorage()
        self.dummy_address_api = DummyAddressApi()
        self.partner_dto = PartnerDto(
            id="valid_id",
            cnpj="valid_cnpj",
            cpf="valid_cpf",
            corporate_name="valid_corporate_name",
            trading_name="valid_trading_name",
            phone="valid_phone",
            email="valid_email",
            cep="valid_cep",
            uf="valid_uf",
            city="valid_city",
        )

    def test_should_bad_request_if_an_invalid_partner_is_provider(self):
        self.partner_dto.cnpj = None
        manager = PartnerManager(self.dummy_storage, self.dummy_address_api)
        response = manager.create_or_update_partners([self.partner_dto])
        self.assertEqual(response, bad_request(response["body"]))

    def test_should_created_if_a_valid_partner_is_provider(self):
        manager = PartnerManager(self.dummy_storage, self.dummy_address_api)
        response = manager.create_or_update_partners([self.partner_dto])
        self.assertEqual(response, created())

    def test_should_return_ok_if_get_all_partners(self):
        manager = PartnerManager(self.dummy_storage, self.dummy_address_api)
        response = manager.get_all_partners()
        self.assertEqual(
            response,
            ok(response["body"]),
        )

    def test_should_return_cnpj_equals_none_on_response_if_cnpj_has_less_than_11_characters(
        self,
    ):
        self.partner_dto.cnpj = "cpf"
        self.partner_dto.cpf = None
        manager = PartnerManager(self.dummy_storage, self.dummy_address_api)
        response = manager.create_or_update_partners([self.partner_dto])
        self.assertEqual(response, created())
        response = manager.get_all_partners()
        self.assertEqual(response["body"][0].cnpj, None)

    def test_should_return_cpf_equals_none_on_response_if_cnpj_has_more_than_11_characters(
        self,
    ):
        self.partner_dto.cnpj = "valid_cnpj_with_more_than_11_characters"
        self.partner_dto.cpf = None
        manager = PartnerManager(self.dummy_storage, self.dummy_address_api)
        response = manager.create_or_update_partners([self.partner_dto])
        self.assertEqual(response, created())
        response = manager.get_all_partners()
        self.assertEqual(response["body"][0].cpf, None)

    def test_should_server_error_if_create_new_partner_throws(self):
        manager = PartnerManager(self.dummy_storage, self.dummy_address_api)
        response = manager.create_or_update_partners(self.partner_dto)
        self.assertEqual(response["status_code"], 500)
        self.assertEqual(str(response["body"]), str(server_error()["body"]))
