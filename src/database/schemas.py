from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, validator
from validate_docbr import CNPJ

from src.utils.exceptions import response_exception


class ZipCodeJsonSchema(BaseModel):
    zip_code: str = Field(alias="cep")
    street: str = Field(alias="logradouro")
    complement: str = Field(alias="complemento")
    district: str = Field(alias="bairro")
    city: str = Field(alias="localidade")
    state: str = Field(alias="uf")
    ibge: str
    gia: str
    area_code: str = Field(alias="ddd")
    siafi: str

    @validator("zip_code")
    def format_zip_code(cls, value):
        zip_code = "".join(filter(str.isdigit, value))
        return zip_code


class ZipCodeSchema(BaseModel):
    zip_code: str = Field(alias="cep")
    district: str = Field(alias="bairro")
    city: str = Field(alias="localidade")
    state: str = Field(alias="uf")
    last_update: datetime

    class Config:
        allow_population_by_field_name = True
        orm_mode: True


class PartnerUpdateSchema(BaseModel):
    company_name: Optional[str] = Field(
        alias="razao_social", example="01234567891234"
    )
    trade_name: Optional[str] = Field(
        alias="nome_fantasia", example="Empresa Exemplo"
    )
    phone: Optional[str] = Field(alias="telefone", example="(12) 3456-7890")
    email: Optional[str] = Field(example="exemplo@email.com")
    zip_code: Optional[str] = Field(alias="cep")

    @validator("zip_code")
    def format_zip_code(cls, value):
        zip_code = "".join(filter(str.isdigit, value))
        return zip_code


class PartnerJsonSchema(PartnerUpdateSchema):
    cnpj: str = Field(example="01.234.567/8912-34")
    zip_code: str = Field(alias="cep", example="12345-678")

    @validator("cnpj")
    def validate_cnpj(cls, value):
        cnpj = "".join(filter(str.isdigit, value))
        if not CNPJ().validate(cnpj):
            response_exception("Invalid CNPJ")
        return cnpj

    @validator("zip_code")
    def format_zip_code(cls, value):
        zip_code = "".join(filter(str.isdigit, value))
        return zip_code


class PartnerSchema(PartnerJsonSchema):
    partner_id: str = Field(alias="id_parceiro")
    zip_code_info: ZipCodeSchema
    last_update: datetime

    class Config:
        allow_population_by_field_name = True
        orm_mode: True
