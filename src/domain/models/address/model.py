from typing import Optional

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from src.domain.models.orm_base.model import Base


class AddressModel(Base):
    __tablename__ = "addresses"
    __table_args__ = {'extend_existing': True}
    id: Mapped[int] = mapped_column(primary_key=True)
    address: Mapped[str] = mapped_column(String(250))
    complement: Mapped[Optional[str]] = mapped_column(String(100))
    neighborhood: Mapped[Optional[str]] = mapped_column(String(30))
    city: Mapped[str] = mapped_column(String(20))
    state: Mapped[str] = mapped_column(String(2))
    partner_cnpj: Mapped[int] = mapped_column(
        ForeignKey("partners.cnpj", ondelete="CASCADE")
    )
