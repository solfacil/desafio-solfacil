import uuid
from datetime import datetime

from sqlalchemy import Column, DateTime, String

from src.database import Base


def get_id():
    return str(uuid.uuid4())


class Parceiro(Base):
    __tablename__ = "tb_parceiros"
    id_parceiro = Column(String, primary_key=True, default=get_id)
    cnpj = Column(String(255), unique=True, nullable=False)
    razao_social = Column(String(255))
    nome_fantasia = Column(String(255))
    telefone = Column(String(255))
    email = Column(String(255))
    cep = Column(String(255), nullable=False)
    data_atualizacao = Column(
        DateTime(), default=datetime.now(), onupdate=datetime.now()
    )
