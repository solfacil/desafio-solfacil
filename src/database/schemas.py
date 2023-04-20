from datetime import datetime
from typing import Optional

from pydantic import BaseModel, validator
from validate_docbr import CNPJ

from src.utils.exceptions import response_exception


class SchemaJsonCepInfo(BaseModel):
    cep: str
    logradouro: str
    complemento: str
    bairro: str
    localidade: str
    uf: str
    ibge: str
    gia: str
    ddd: str
    siafi: str


class SchemaCepInfo(BaseModel):
    cep: str
    bairro: str
    localidade: str
    uf: str
    data_atualizacao: datetime

    class Config:
        orm_mode: True


class SchemaUpdateParceiro(BaseModel):
    razao_social: Optional[str]
    nome_fantasia: Optional[str]
    telefone: Optional[str]
    email: Optional[str]
    cep: Optional[str]

    @validator("cep")
    def formata_cep(cls, value):
        cep = "".join(filter(str.isdigit, value))
        return cep


class SchemaJsonParceiro(SchemaUpdateParceiro):
    cnpj: str
    cep: str

    @validator("cnpj")
    def validate_cnpj(cls, value):
        cnpj = "".join(filter(str.isdigit, value))
        cnpj_verify = CNPJ()
        if not cnpj_verify.validate(cnpj):
            response_exception("cnpj invalid")
        return cnpj

    @validator("cep")
    def formata_cep(cls, value):
        cep = "".join(filter(str.isdigit, value))
        return cep


class SchemaParceiro(SchemaJsonParceiro):
    id_parceiro: str
    cep_info: SchemaCepInfo
    data_atualizacao: datetime

    class Config:
        orm_mode: True
