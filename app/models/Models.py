from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from ..database.connection import Base

class Customers(Base):
    __tablename__ = "clientes"

    cliente_id = Column(Integer, primary_key=True, index=True)
    razao_social = Column(String, unique=True, index=True)
    email = Column(String, default=None)
    nome_fantasia = Column(String, default=None)
    telefone = Column(String, default=None)
    cpf = Column(String, default=None)
    cnpj = Column(String, default=None)

    enderecos = relationship("Adresses", back_populates="proprietario")


class Adresses(Base):
    __tablename__ = "enderecos"

    endereco_id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("clientes.cliente_id"))
    cep = Column(String, nullable=False)
    logradouro = Column(String, default=None)
    complemento = Column(String, default=None)
    bairro = Column(String, default=None)
    localidade = Column(String, default=None)
    uf = Column(String, default=None)
    ibge = Column(Integer, default=None)

    proprietario = relationship("Customers", back_populates="enderecos")
