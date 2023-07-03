from typing import Optional

from sqlalchemy import ForeignKey, String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.domain.models.orm_base.model import Base


class PartnerModel(Base):
    __tablename__ = "partners"
    cnpj: Mapped[str] = mapped_column(String(14), primary_key=True)
    company_name: Mapped[str] = mapped_column(String(100))
    fantasy_name: Mapped[str] = mapped_column(String(100))
    phone: Mapped[Optional[str]] = mapped_column(String(11))
    email: Mapped[Optional[str]] = mapped_column(String(100))
    zipcode: Mapped[Optional[str]] = mapped_column(String(8))
    # zipcode: Mapped[Optional["AddressModel"]] = relationship(back_populates="zipcode")
