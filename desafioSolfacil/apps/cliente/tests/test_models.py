from django.test import TestCase
from apps.cliente.models import ClienteModel


class ClienteTestModel(TestCase):

    def test_create_client(self):
        client = ClienteModel.objects.create(cnpj='01.001.001/0001-01')
        self.assertEquals(client.cnpj, '01.001.001/0001-01')
