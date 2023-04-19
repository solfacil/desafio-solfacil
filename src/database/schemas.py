from datetime import datetime
from typing import Union

from pydantic import BaseModel


class SchemaParceiro(BaseModel):
    id_parceiro = str
    cnpj = str
    razao_social = Union[str, None] = None
    nome_fantasia = Union[str, None] = None
    telefone = Union[str, None] = None
    email = Union[str, None] = None
    cep = str
    data_atualizacao: datetime
