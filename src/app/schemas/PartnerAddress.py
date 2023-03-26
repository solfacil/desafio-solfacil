from typing import Optional

from loguru import logger  # noqa: F401
from schemas.Base import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

# from schemas import Partner


class PartnerAddress(Base):
    __tablename__ = "partner_address"

    id: Mapped[int] = mapped_column(primary_key=True)
    cep: Mapped[str]
    logradouro: Mapped[Optional[str]]
    complemento: Mapped[Optional[str]]
    bairro: Mapped[Optional[str]]
    localidade: Mapped[Optional[str]]
    uf: Mapped[Optional[str]]
    ibge: Mapped[Optional[str]]
    gia: Mapped[Optional[str]]
    ddd: Mapped[Optional[str]]
    siafi: Mapped[Optional[str]]

    partner_id: Mapped[int] = mapped_column(ForeignKey("partner.id"))  # __tablename__.<primary_key>
    # partner: Mapped["Partner"] = relationship(back_populates="address")
