import uuid

from django.db import models


class Partner(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cnpj = models.CharField(max_length=14, blank=False, null=True)
    cpf = models.CharField(max_length=11, blank=False, null=True)
    corporate_name = models.CharField(max_length=250, blank=False, null=False)
    trading_name = models.CharField(max_length=250, blank=False, null=True)
    phone = models.CharField(max_length=11, blank=False, null=True)
    email = models.CharField(max_length=250, blank=False, null=False)
    cep = models.CharField(max_length=8, blank=False, null=False)
    uf = models.CharField(max_length=2, blank=False, null=True)
    city = models.CharField(max_length=100, blank=False, null=True)
