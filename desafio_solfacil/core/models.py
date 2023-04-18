import uuid

from django.conf import settings
from django.core.mail import send_mail
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from desafio_solfacil.core.validators import validate_cpf_or_cnpj


# Create your models here.


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Parceiro(BaseModel):
    cnpj = models.CharField(
        max_length=18, unique=True, validators=[validate_cpf_or_cnpj]
    )
    razao_social = models.CharField(max_length=255)
    nome_fantasia = models.CharField(max_length=255, blank=True, null=True)
    if settings.USE_PHONENUMBER_FIELD:
        telefone = PhoneNumberField(blank=True, null=True)
    else:
        telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField()
    cep = models.CharField(max_length=9)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=2)
    endereco = models.CharField(max_length=255)

    def enviar_email_boas_vindas(self):
        send_mail(
            subject="Bem-vindo ao Solfácil",
            message="Olá, seja bem-vindo ao Solfácil!",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[self.email],
        )
