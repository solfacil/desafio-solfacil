from loguru import logger  # noqa: F401
from schemas.Base import Base
from schemas.PartnerAddress import PartnerAddress
from schemas.PartnerContact import PartnerContact
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Partner(Base):
    __tablename__ = "partner"

    id: Mapped[int] = mapped_column(primary_key=True)
    cnpj: Mapped[str]
    razao_social: Mapped[str]
    nome_fantasia: Mapped[str]
    address: Mapped["PartnerAddress"] = relationship(lazy='selectin')
    contact: Mapped["PartnerContact"] = relationship(lazy='selectin')
