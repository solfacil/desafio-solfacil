from sqlalchemy.orm import Session

from src.database import schemas
from src.database.models import Parceiro


def consultar_parceiros(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Parceiro).offset(skip).limit(limit).all()


def criar_parceiro(db: Session, parceiro: schemas.SchemaJsonParceiro):
    novo_parceiro = Parceiro(**parceiro.dict())
    db.add(novo_parceiro)
    db.commit()
    db.refresh(novo_parceiro)
    return novo_parceiro


def atualizar_parceiro(
    db: Session, cnpj, parceiro: schemas.SchemaJsonParceiro
):
    db_parceiro = db.query(Parceiro).filter(Parceiro.cnpj == cnpj).first()
    if not db_parceiro:
        raise Exception("Not Found")
    for field, value in parceiro.dict(exclude_unset=True).items():
        setattr(db_parceiro, field, value)
    db.add(db_parceiro)
    db.commit()
    db.refresh(db_parceiro)

    return db_parceiro


def deletar_parceiro(db: Session, cnpj):
    db_parceiro = db.query(Parceiro).filter(Parceiro.cnpj == cnpj).first()
    if not db_parceiro:
        raise Exception("Not Found")
    db.delete(db_parceiro)
    db.commit()

    return db_parceiro
