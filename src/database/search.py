from sqlalchemy import or_
from sqlalchemy.orm import Session

from src.database.models import Partner


def consult_partner_cnpj(db: Session, cnpj: str):
    partner = db.query(Partner).filter(Partner.cnpj == cnpj).first()
    if partner is None:
        raise Exception("Not Found Partner")
    return partner


def search_partner(db: Session, query: str, skip: int = 0, limit: int = 100):
    result = (
        db.query(Partner)
        .filter(
            or_(
                Partner.cnpj.ilike(f"%{query}%"),
                Partner.company_name.ilike(f"%{query}%"),
                Partner.trade_name.ilike(f"%{query}%"),
                Partner.phone.ilike(f"%{query}%"),
                Partner.email.ilike(f"%{query}%"),
                Partner.zip_code.ilike(f"%{query}%"),
            )
        )
        .offset(skip)
        .limit(limit)
        .all()
    )
    return result
