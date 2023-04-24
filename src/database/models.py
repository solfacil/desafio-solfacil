import uuid
from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, String
from sqlalchemy.inspection import inspect
from sqlalchemy.orm import relationship

from src.database import Base


def get_id():
    return str(uuid.uuid4())


class SerializerPartner(object):
    def serialize(self):
        partner = {c: getattr(self, c) for c in inspect(self).attrs.keys()}
        zip_code_info = {
            c: getattr(self.zip_code_info, c)
            for c in inspect(self.zip_code_info).attrs.keys()
        }
        partner["zip_code_info"] = zip_code_info

        return partner


class Partner(Base):
    __tablename__ = "tb_partners"
    partner_id = Column(String, primary_key=True, default=get_id)
    cnpj = Column(String(14), unique=True, nullable=False)
    company_name = Column(String(100))
    trade_name = Column(String(100))
    phone = Column(String(30))
    email = Column(String(50))
    zip_code = Column(
        String(10),
        ForeignKey("tb_zip_code_info.zip_code"),
        nullable=False,
    )
    zip_code_info = relationship(
        "ZipCodeInfo", foreign_keys=[zip_code], uselist=False
    )
    last_update = Column(
        DateTime(), default=datetime.now(), onupdate=datetime.now()
    )

    def serialize(self):
        d = SerializerPartner.serialize(self)
        return d


class ZipCodeInfo(Base):
    __tablename__ = "tb_zip_code_info"
    zip_code_id = Column(String, primary_key=True, default=get_id)
    zip_code = Column(String(10), unique=True, nullable=False)
    street = Column(String(100), nullable=False)
    complement = Column(String(255), nullable=False)
    district = Column(String(100), nullable=False)
    city = Column(String(100), nullable=False)
    state = Column(String(5), nullable=False)
    ibge = Column(String(100), nullable=False)
    gia = Column(String(100), nullable=False)
    area_code = Column(String(5), nullable=False)
    siafi = Column(String(100), nullable=False)
    last_update = Column(
        DateTime(), default=datetime.now(), onupdate=datetime.now()
    )
