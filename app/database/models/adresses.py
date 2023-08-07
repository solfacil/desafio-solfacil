from sqlalchemy import Column, ForeignKey, Integer, String

from app.database.connection import Base


class Adresses(Base):
    __tablename__ = "enderecos"

    endereco_id = Column(Integer, primary_key=True, index=True)
    cep = Column(Integer, ForeignKey("clientes.cep"), nullable=False)
    logradouro = Column(String, default=None)
    complemento = Column(String, default=None)
    bairro = Column(String, default=None)
    localidade = Column(String, default=None)
    uf = Column(String, default=None)
    ibge = Column(Integer, default=None)
