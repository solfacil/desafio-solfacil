from django.db import models


class Parceiro(models.Model):
    cnpj = models.CharField(max_length=100)
    razao_social = models.CharField(max_length=100)
    nome_fantasia = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    cep = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome_fantasia
    
class Endereco(models.Model):
    parceiro = models.ForeignKey(Parceiro, on_delete=models.CASCADE)
    cep = models.CharField(max_length=100)
    logradouro = models.CharField(max_length=100, blank=True)
    complemento = models.CharField(max_length=100, blank=True)
    bairro = models.CharField(max_length=100, blank=True)
    cidade = models.CharField(max_length=100, blank=True)
    estado = models.CharField(max_length=2, blank=True)

    def __str__(self):
        return f"{self.logradouro}, {self.numero} - {self.cidade}/{self.estado}"