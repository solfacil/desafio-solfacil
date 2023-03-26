import re

from loguru import logger  # noqa: F401
from pydantic import BaseModel, validator
from validate_docbr import CNPJ

from .PartnerAddress import PartnerAddress
from .PartnerContact import PartnerContact


class CreatePartner(BaseModel):
    cnpj: str
    razao_social: str
    nome_fantasia: str
    address: PartnerAddress
    contact: PartnerContact

    @validator('razao_social', pre=True)
    def validate_razao_social(cls, v: str):
        v = v.encode('utf-8')
        return v

    @validator('nome_fantasia', pre=True)
    def validate_nome_fantasia(cls, v: str):
        v = v.encode('utf-8')
        return v

    @validator('cnpj', pre=True)
    def validate_cnpj(cls, v):
        # Remove all non-digit characters from the string
        cnpj_numbers = re.sub(r'[^\d]', '', v)
        cnpj_numbers = str(cnpj_numbers)
        cnpj = CNPJ()
        if not cnpj.validate(cnpj_numbers):
            raise ValueError(f"The CNPJ '{cnpj_numbers}' is invalid.")

        return cnpj_numbers
