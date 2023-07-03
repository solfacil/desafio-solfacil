from typing import Optional

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.domain.models.orm_base.model import Base


class PartnerModel(Base):
    __tablename__ = "partners"
    __table_args__ = {'extend_existing': True}
    cnpj: Mapped[str] = mapped_column(String(14), primary_key=True)
    company_name: Mapped[str] = mapped_column(String(100))
    fantasy_name: Mapped[str] = mapped_column(String(100))
    phone: Mapped[Optional[str]] = mapped_column(String(11))
    email: Mapped[Optional[str]] = mapped_column(String(100))
    zipcode: Mapped[Optional[str]] = mapped_column(String(8))
