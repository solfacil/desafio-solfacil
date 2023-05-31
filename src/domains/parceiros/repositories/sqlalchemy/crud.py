from uuid import uuid4

from sqlalchemy.orm import Session

from . import models, schemas


def get_parceiros(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Parceiro).offset(skip).limit(limit).all()


def create_parceiro(db: Session, parceiro: schemas.Parceiro):
    db_parceiro = models.Parceiro(
        id_=uuid4(),
        cnpj=parceiro["cnpj"],
        razao_social=parceiro["razao_social"],
        nome_fantasia=parceiro["nome_fantasia"],
        telefone=parceiro["telefone"],
        email=parceiro["email"],
        cidade=parceiro["cidade"],
        estado=parceiro["estado"],
        cep=parceiro["cep"],
    )
    db.add(db_parceiro)
    db.commit()
    db.refresh(db_parceiro)
    return db_parceiro


def get_parceiro_by_cnpj(
    db: Session, Parceiro: schemas.Parceiro, parceiro: schemas.Parceiro
):
    db_parceiro = db.query(Parceiro).get({"cnpj": parceiro["cnpj"]})
    return db_parceiro


def update_parceiro(
    db: Session, parceiro: schemas.Parceiro, updated_parceiro_data: schemas.Parceiro
):
    parceiro.razao_social = updated_parceiro_data["razao_social"]
    parceiro.nome_fantasia = updated_parceiro_data["nome_fantasia"]
    parceiro.telefone = updated_parceiro_data["telefone"]
    parceiro.email = updated_parceiro_data["email"]
    parceiro.cep = updated_parceiro_data["cep"]
    db.commit()
    db.close()
