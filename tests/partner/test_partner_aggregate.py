import unittest

from api.domain.partner.entities import Partner
from api.domain.partner.exceptions import MissingParamError


class PartnerAggregateTests(unittest.TestCase):
    def setUp(self):
        self.partner = Partner(
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

    def test_should_raise_missing_param_error_if_no_corporate_name_is_provided(self):
        self.partner.corporate_name = None
        self.assertRaises(MissingParamError, self.partner.is_valid)

    def test_should_raise_missing_param_error_if_no_cep_name_is_provided(self):
        self.partner.cep = None
        self.assertRaises(MissingParamError, self.partner.is_valid)

    def test_should_raise_missing_param_error_if_no_email_name_is_provided(self):
        self.partner.email = None
        self.assertRaises(MissingParamError, self.partner.is_valid)

    def test_should_raise_missing_param_error_if_no_cnpj_name_is_provided(self):
        self.partner.cnpj = None
        self.assertRaises(MissingParamError, self.partner.is_valid)
