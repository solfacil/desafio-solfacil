from django.test import TestCase
from apps.cliente.models import ClienteModel


class ClienteTestViews(TestCase):

    def test_get_all_clients(self):
        clients = ClienteModel.objects.all()
        self.assertIsNotNone(clients)

    def test_get_one_client_by_razao_social(self):
        client = ClienteModel.objects.create(razao_social='Teste Unitario')
        clients = ClienteModel.objects.filter(razao_social='Teste Unitario')
        self.assertIn(client, clients)
