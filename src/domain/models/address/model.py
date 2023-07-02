from datetime import datetime

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column

from src.domain.models.orm_base.model import Base


class PartnerModel(Base):
    __tablename__ = "partners"

    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    cnpj: Mapped[str]
    company_name: Mapped[str]
    fantasy_name: Mapped[str]
    phone: Mapped[str]
    email: Mapped[str]


class AddressModel(Base):
    __tablename__ = "address"
    id: Mapped[int] = mapped_column(primary_key=True)
    partner_id: Mapped[int] = mapped_column(ForeignKey("partners.id"))
    address: Mapped[str]
    number: Mapped[str]
    complement: Mapped[str]
    city: Mapped[str]
    state: Mapped[str]
    zipcode: Mapped[str]
    