from loguru import logger  # noqa: F401
from pydantic import BaseModel

from .PartnerAddress import PartnerAddress
from .PartnerContact import PartnerContact


class ListPartner(BaseModel):
    id: int
    cnpj: str
    razao_social: str
    nome_fantasia: str
    address: PartnerAddress
    contact: PartnerContact

    class Config:
        orm_mode = True
