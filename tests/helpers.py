import random
import re
import string
from dataclasses import dataclass


def generate_cnpj():
    """https://gist.github.com/lucascnr/24c70409908a31ad253f97f9dd4c6b7c"""

    def calculate_special_digit(cnpj):
        digit = 0
        for i, v in enumerate(cnpj):
            digit += v * (i%8 + 2)
        digit = 11 - digit%11
        return digit if digit < 10 else 0

    cnpj = [1, 0, 0, 0] + [random.randint(0, 9) for x in range(8)]
    for _ in range(2):
        cnpj = [calculate_special_digit(cnpj)] + cnpj

    return '%s%s.%s%s%s.%s%s%s/%s%s%s%s-%s%s' % tuple(cnpj[::-1])


@dataclass
class PartnerFactory:
    """Generate random data for CreatePartner tests"""
    cnpj: str
    razao_social: str
    nome_fantasia: str
    cep: str
    telefone: str
    email: str

    @classmethod
    def generate(cls):
        valid_ceps = ['72242-165', '89068-168', '77066-222', '69901-722', '65055-627']
        return cls(
            cnpj=generate_cnpj(),
            razao_social=''.join(random.choices(string.ascii_letters + string.digits, k=10)),
            nome_fantasia=''.join(random.choices(string.ascii_letters + string.digits, k=10)),
            cep=random.choice(valid_ceps),
            telefone=''.join(random.choices(string.digits, k=11)),
            email=''.join(random.choices(string.ascii_letters + string.digits, k=10))
        )

    @property
    def clean_cnpj(self):
        return re.sub(r'[^\d]', '', self.cnpj)

    @property
    def body(self):
        return {
            'cnpj': self.cnpj,
            'razao_social': self.razao_social,
            'nome_fantasia': self.nome_fantasia,
            'address': {'cep': self.cep},
            'contact': {'telefone': self.telefone, 'email': self.email}
        }  # yapf: disable
