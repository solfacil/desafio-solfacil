import uuid
from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, String
from sqlalchemy.inspection import inspect
from sqlalchemy.orm import relationship

from src.database import Base


def get_id():
    return str(uuid.uuid4())


class SerializerParceiro(object):
    def serialize(self):
        parceiro = {c: getattr(self, c) for c in inspect(self).attrs.keys()}
        cep_info = {
            c: getattr(self.cep_info, c)
            for c in inspect(self.cep_info).attrs.keys()
        }
        parceiro["cep_info"] = cep_info

        return parceiro


class Parceiro(Base):
    __tablename__ = "tb_parceiros"
    id_parceiro = Column(String, primary_key=True, default=get_id)
    cnpj = Column(String(14), unique=True, nullable=False)
    razao_social = Column(String(100))
    nome_fantasia = Column(String(100))
    telefone = Column(String(30))
    email = Column(String(50))
    cep = Column(String(10), ForeignKey("tb_cep_info.cep"), nullable=False)
    cep_info = relationship("CepInfo", foreign_keys=[cep], uselist=False)
    data_atualizacao = Column(
        DateTime(), default=datetime.now(), onupdate=datetime.now()
    )

    def serialize(self):
        d = SerializerParceiro.serialize(self)
        return d


class CepInfo(Base):
    __tablename__ = "tb_cep_info"
    id_cep = Column(String, primary_key=True, default=get_id)
    cep = Column(String(10), unique=True, nullable=False)
    logradouro = Column(String(100), nullable=False)
    complemento = Column(String(255), nullable=False)
    bairro = Column(String(100), nullable=False)
    localidade = Column(String(100), nullable=False)
    uf = Column(String(5), nullable=False)
    ibge = Column(String(100), nullable=False)
    gia = Column(String(100), nullable=False)
    ddd = Column(String(5), nullable=False)
    siafi = Column(String(100), nullable=False)
    data_atualizacao = Column(
        DateTime(), default=datetime.now(), onupdate=datetime.now()
    )
