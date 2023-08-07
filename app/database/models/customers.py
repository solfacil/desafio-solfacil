from typing import Optional
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped

from app.database.models.adresses import Adresses
from app.database.connection import Base


class Customers(Base):
    __tablename__ = "clientes"

    cliente_id = Column(Integer, primary_key=True, index=True)
    razao_social = Column(String, unique=True, index=True)
    email = Column(String, default=None)
    nome_fantasia = Column(String, default=None)
    telefone = Column(String, default=None)
    cpf = Column(String, default=None)
    cnpj = Column(String, default=None)
    cep = Column(Integer, default=None)
    tipo_pessoa = Column(String, nullable=False)
    enderecos = Mapped[Optional["Adresses"]]
