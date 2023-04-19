from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class SchemaCriacaoParceiro(BaseModel):
    cnpj: str
    razao_social: Optional[str]
    nome_fantasia: Optional[str]
    telefone: Optional[str]
    email: Optional[str]
    cep: str


class SchemaParceiro(SchemaCriacaoParceiro):
    id_parceiro: str
    data_atualizacao: datetime

    class Config:
        orm_mode: True
