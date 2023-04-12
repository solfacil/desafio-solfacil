import json
from unittest.mock import patch

from django.test import TestCase

from api.models import Parceiro
from api.repository import ParceiroRepository
from api.utils import get_address_by_cep


class GetAddressByCepTestCase(TestCase):

    @patch('api.utils.requests.get')
    def test_get_address_by_cep_valid(self, mock_get):
        mock_response = {"cep": "12345-678", "logradouro": "Rua Exemplo", "bairro": "Centro", "localidade": "São Paulo", "uf": "SP"}
        mock_get.return_value.content.decode.return_value = json.dumps(mock_response)

        address = get_address_by_cep("12345678")

        self.assertEqual(address, mock_response)

    @patch('api.utils.requests.get')
    def test_get_address_by_cep_invalid(self, mock_get):
        mock_response = {"erro": True}
        mock_get.return_value.content.decode.return_value = json.dumps(mock_response)

        address = get_address_by_cep("invalid_cep")

        self.assertIsNone(address)

class SavePartnerTestCase(TestCase):
    
    def test_save_partner(self):
        partner_obj = {
            'cnpj': '12345678901234',
            'razao_social': 'Empresa Teste',
            'nome_fantasia': 'Teste',
            'telefone': '11123456789',
            'email': 'teste@teste.com.br',
            'cep': '12345678'
        }

        ParceiroRepository.save_partner(partner_obj)

        partner = Parceiro.objects.filter(cnpj='12345678901234').first()
        self.assertIsNotNone(partner)
        self.assertEqual(partner.razao_social, 'Empresa Teste')
        self.assertEqual(partner.nome_fantasia, 'Teste')
        self.assertEqual(partner.telefone, '11123456789')
        self.assertEqual(partner.email, 'teste@teste.com.br')
        self.assertEqual(partner.cep, '12345678')
