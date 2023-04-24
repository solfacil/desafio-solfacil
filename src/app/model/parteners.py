from sqlalchemy import Column, Integer, String, DateTime,JSON

from ..database.database import Base

import datetime



class Partener(Base):
    __tablename__ = "partener"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    razao_social = Column(String(255), index=True)
    cnpj = Column(String(20), unique=True, index=True)
    email = Column(String(255), unique=True, index=True)
    phone_number = Column(String(20), index=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow,onupdate=datetime.datetime.utcnow)
    address =  Column(JSON)
