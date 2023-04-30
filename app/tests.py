from django.test import TestCase, Client
from django.urls import reverse
from .models import Partner, PartnerAddress
from django.core.files.uploadedfile import SimpleUploadedFile

class PartnerTestCase(TestCase):
    def setUp(self):
         self.partner = Partner.objects.create(
            cnpj='16.470.954/0001-06',
            razao_social = 'Test Razao Social',
            nome_fantasia='Test Partner',
            telefone='1234567890',
            email='test@example.com',
            cep='12345-678'
        )

    def test_cnpj_max_length(self):
        partner = Partner.objects.get(id=1)
        max_length = partner._meta.get_field('cnpj').max_length
        self.assertEqual(max_length, 14)

    def test_cnpj_valid(self):
        partner = Partner.objects.get(id=1)
        cnpj_ = partner.cnpj
        cnpj = ''.join(filter(str.isdigit, cnpj_))
        self.assertTrue(cnpj.isdigit())

    def test_email_valid(self):
        partner = Partner.objects.get(id=1)
        email = partner.email
        self.assertTrue('@' in email and '.' in email)

    def test_telefone_valid(self):
        partner = Partner.objects.get(id=1)
        telefone = partner.telefone
        self.assertTrue(telefone.isdigit())

    def test_cep_max_length(self):
        partner = Partner.objects.get(id=1)
        max_length = partner._meta.get_field('cep').max_length
        self.assertEqual(max_length, 9)

class PartnerAddressTestCase(TestCase):
    def setUp(self):
        self.partner = Partner.objects.create(
            cnpj='12345678901234',
            razao_social = 'Test Razao Social',
            nome_fantasia='Test Partner',
            telefone='1234567890',
            email='test@example.com',
            cep='12345-678'
        )
        self.partnerAddress = PartnerAddress.objects.create(
            partner=self.partner,
            cep = '12345-678',
            logradouro = ' test logradouro',
            complemento = 'test complemento  22',
            localidade = ' test localidade',
            uf = 'TT',
            ibge = 'test IBGE',
            gia = 'test gia',
            ddd = '222',
            siafi = 'Test Siafi'
        )

    def test_cep_max_length(self):
        partner =PartnerAddress.objects.get(id=1)
        max_length = partner._meta.get_field('cep').max_length
        self.assertEqual(max_length, 9)

    def test_uf_max_length(self):
        partnerAddress = PartnerAddress.objects.get(id=1)
        max_length = partnerAddress._meta.get_field('uf').max_length
        self.assertEqual(max_length, 2)

    def test_ddd_max_length(self):
        partnerAddress = PartnerAddress.objects.get(id=1)
        max_length = partnerAddress._meta.get_field('ddd').max_length
        self.assertEqual(max_length, 3)


class MyViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('upload_csv')

    def test_partner_list(self):
        client = Client()
        response = client.get(reverse('partners-list'))
        self.assertEqual(response.status_code, 200)

    def test_partner_address_list(self):
        client = Client()
        response = client.get(reverse('partners-address-list'))
        self.assertEqual(response.status_code, 200)

    def test_upload_csv(self):
        csv_file = SimpleUploadedFile("file.csv", b"file_content", content_type="text/csv")
        
        response = self.client.post(self.url, {'csv_file': csv_file})

        self.assertEqual(response.status_code, 200)
