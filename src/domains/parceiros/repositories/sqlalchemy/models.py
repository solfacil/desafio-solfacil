import uuid

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

from .database import Base


class Parceiro(Base):
    __tablename__ = "parceiro"

    id_ = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    cnpj = Column(String, unique=True, index=True)
    razao_social = Column(String)
    nome_fantasia = Column(String)
    telefone = Column(String)
    email = Column(String, unique=True)
    cidade = Column(String)
    estado = Column(String)
    cep = Column(String)
