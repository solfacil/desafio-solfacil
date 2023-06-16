from typing import Optional
from pydantic import BaseModel
from .Address import Address

class CustomerBase(BaseModel):
    razao_social: str
    email: Optional[str] = None
    nome_fantasia: Optional[str] = None
    telefone: Optional[str] = None
    cpf: Optional[str] = None
    cnpj: Optional[str] = None

class CustomerData(CustomerBase):
    pass

class Customer(CustomerBase):
    cliente_id: Optional[int] = None
    enderecos: list[Address] = []

    class Config:
        orm_mode = True
