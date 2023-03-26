from typing import Optional

from loguru import logger  # noqa: F401
from schemas.Base import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

# from schemas import Partner


class PartnerContact(Base):
    __tablename__ = "partner_contact"

    id: Mapped[int] = mapped_column(primary_key=True)
    telefone: Mapped[Optional[str]]
    email: Mapped[Optional[str]]

    partner_id: Mapped[int] = mapped_column(ForeignKey("partner.id"))  # __tablename__.<primary_key>
    # partner: Mapped["Partner"] = relationship(back_populates="address")
