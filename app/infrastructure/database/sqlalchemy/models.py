from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class ParceiroModel(Base):
    __tablename__ = "parceiro"

    id = Column(Integer, primary_key=True, index=True)
    cnpj = Column(String, unique=True, index=True, nullable=False)
    razao_social = Column(String, nullable=False)
    nome_fantasia = Column(String)
    telefone = Column(String)
    email = Column(String, nullable=False)
    cep = Column(String, nullable=False)
    cidade  = Column(String, nullable=True)
    estado = Column(String, nullable=True)
