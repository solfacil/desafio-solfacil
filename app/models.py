from django.db import models
from django.forms import ValidationError

class Partner(models.Model):
    cnpj = models.CharField(max_length=14, unique=True)
    razao_social = models.CharField(max_length=100)
    nome_fantasia = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    cep = models.CharField(max_length=9)
   
    def clean(self):
        # Validation for CNPJ
        self.cnpj = ''.join(filter(str.isdigit, value))
        if not self.cnpj.isdigit() or len(self.cnpj) != 14:
            raise ValidationError("CNPJ must be a 14-digit number")

        # Validation for phone number
        if not self.phone.isdigit() or len(self.phone) < 8 or len(self.phone) > 20:
            raise ValidationError("Phone number must be between 8 and 20 digits")

        # Validation for CEP
        self.cep.replace('-', '')
        if not self.cep.isdigit() or len(self.cep) !=8:
            raise ValidationError("CEP must be an 8 digits number")

class PartnerAddress(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    cep = models.CharField(max_length=9)
    logradouro = models.CharField(max_length=100)
    complemento = models.CharField(max_length=100)
    localidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)
    ibge = models.CharField(max_length=100)
    gia = models.CharField(max_length=100)
    ddd = models.CharField(max_length=3)
    siafi = models.CharField(max_length=100)