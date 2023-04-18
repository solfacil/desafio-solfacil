from django.conf import settings
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITransactionTestCase

from services.viacep_api import ViaCepApi


# Create your tests here.


class ParceiroTestCase(APITransactionTestCase):
    def test_import(self):
        url = reverse("parceiros-import_parceiros")
        with open(settings.BASE_DIR / "assets/exemplo.csv", "rb") as f:
            response = self.client.post(url, {"data": f})
            self.assertEqual(response.status_code, 201)
            self.assertEqual(
                response.data["mensagem"],
                "Foram encontrados erros na importação",
            )
            self.assertEqual(len(response.data["errors"]), 3)
            self.assertEqual(len(response.data["data"]), 2)


class ViaCepTestCase(TestCase):
    def test_cep(self):
        validation_data = {
            "cep": "58046-720",
            "logradouro": "Rua Aluísio Bezerra da Silva",
            "complemento": "(Lot Q Mares II)",
            "bairro": "Portal do Sol",
            "localidade": "João Pessoa",
            "uf": "PB",
            "ibge": "2507507",
            "gia": "",
            "ddd": "83",
            "siafi": "2051",
        }

        via_cep = ViaCepApi()
        response = via_cep.get_address(validation_data["cep"])
        self.assertEqual(response, validation_data)
