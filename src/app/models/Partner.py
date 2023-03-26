from loguru import logger  # noqa: F401
from pydantic import BaseModel


class Partner(BaseModel):
    cnpj: str
    razao_social: str
    nome_fantasia: str

    class Config:
        orm_mode = True

    # @validator('cnpj', pre=True)
    # def validate_cnpj(cls, v):
    #     # Remove all non-digit characters from the string
    #     cnpj_numbers = re.sub(r'[^\d]', '', v)
    #     cnpj_numbers = str(cnpj_numbers)
    #     cnpj = CNPJ()
    #     if not cnpj.validate(cnpj_numbers):
    #         raise ValueError(f"The CNPJ '{cnpj_numbers}' is invalid.")

    #     return cnpj_numbers
