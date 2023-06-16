from typing import Optional
from pydantic import BaseModel

class AddressBase(BaseModel):
    cep: Optional[str] = None
    logradouro: Optional[str] = None
    complemento: Optional[str] = None
    bairro: Optional[str] = None
    localidade: Optional[str] = None
    uf: Optional[str] = None
    ibge: Optional[str] = None

class AddressData(AddressBase):
    pass

class Address(AddressBase):
    endereco_id: Optional[int] = None
    cliente_id: Optional[int] = None

    class Config:
        orm_mode = True
