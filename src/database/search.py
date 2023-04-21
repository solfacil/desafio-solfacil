from sqlalchemy import or_
from sqlalchemy.orm import Session

from src.database.models import Parceiro


def consult_partner_cnpj(db: Session, cnpj_parceiro: str):
    parceiro = (
        db.query(Parceiro).filter(Parceiro.cnpj == cnpj_parceiro).first()
    )
    if parceiro is None:
        raise Exception("Not found")
    return parceiro


def search_partner(db: Session, query: str, skip: int = 0, limit: int = 100):
    resultados = (
        db.query(Parceiro)
        .filter(
            or_(
                Parceiro.cnpj.ilike(f"%{query}%"),
                Parceiro.razao_social.ilike(f"%{query}%"),
                Parceiro.nome_fantasia.ilike(f"%{query}%"),
                Parceiro.telefone.ilike(f"%{query}%"),
                Parceiro.email.ilike(f"%{query}%"),
                Parceiro.cep.ilike(f"%{query}%"),
            )
        )
        .offset(skip)
        .limit(limit)
        .all()
    )
    return resultados
