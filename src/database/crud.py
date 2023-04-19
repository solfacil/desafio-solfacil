from sqlalchemy.orm import Session

from src.database import schemas
from src.database.models import Parceiro


def consultar_parceiros(db: Session):
    return db.query(Parceiro).all()


def criar_parceiro(db: Session, parceiro: schemas.SchemaCriacaoParceiro):
    novo_parceiro = Parceiro(**parceiro.dict())
    db.add(novo_parceiro)
    db.commit()
    return novo_parceiro
