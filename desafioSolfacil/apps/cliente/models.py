from django.db import models


class ClienteModel(models.Model):
    cpf = models.CharField(max_length=14, null=True, blank=True)
    cnpj = models.CharField(max_length=18, null=True, blank=True)
    razao_social = models.CharField(max_length=200, null=True, blank=True)
    nome_fantasia = models.CharField(max_length=200, null=True, blank=True)
    telefone = models.CharField(max_length=16, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    cep = models.CharField(max_length=9, null=True, blank=True)
    cidade = models.CharField(max_length=100, null=True, blank=True)
    estado = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self) -> str:
        return self.razao_social
