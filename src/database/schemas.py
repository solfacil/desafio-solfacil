from datetime import datetime
from typing import Union

from pydantic import BaseModel


class SchemaParceiro(BaseModel):
    id_parceiro: str
    cnpj: str
    razao_social: Union[str, None]
    nome_fantasia: Union[str, None]
    telefone: Union[str, None]
    email: Union[str, None]
    cep: str
    data_atualizacao: datetime


class SchemaCriacaoParceiro(BaseModel):
    cnpj: str
    razao_social: Union[str, None]
    nome_fantasia: Union[str, None]
    telefone: Union[str, None]
    email: Union[str, None]
    cep: str
