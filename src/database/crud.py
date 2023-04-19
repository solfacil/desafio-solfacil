from sqlalchemy.orm import Session

from src.database import schemas
from src.database.models import Parceiro


def consultar_parceiros(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Parceiro).offset(skip).limit(limit).all()


def consultar_parceiro_cnpj(db: Session, cnpj: str):
    return db.query(Parceiro).filter(Parceiro.cnpj == cnpj).first()


def criar_parceiro(db: Session, parceiro: schemas.SchemaCriacaoParceiro):
    novo_parceiro = Parceiro(**parceiro.dict())
    db.add(novo_parceiro)
    db.commit()
    db.refresh(novo_parceiro)
    return novo_parceiro
