from sqlalchemy.orm import Session

from src.database import schemas
from src.database.models import Partner
from src.utils.zip_code_search import verify_zip_code


def list_partners(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Partner).offset(skip).limit(limit).all()


def create_partner(db: Session, partner: schemas.PartnerJsonSchema) -> Partner:
    new_partner = Partner(**partner.dict())
    if verify_zip_code(db, new_partner.zip_code):
        db.add(new_partner)
        db.commit()
        db.refresh(new_partner)
    else:
        raise Exception("Invalid Zip Code")
    return new_partner


def update_partner(
    db: Session,
    cnpj: str,
    partner: schemas.PartnerJsonSchema,
    create_if_not_exists: bool = False,
) -> Partner:
    partner_found = db.query(Partner).filter(Partner.cnpj == cnpj).first()
    if not partner_found:
        if create_if_not_exists:
            return create_partner(db, partner)
        raise Exception("Not Found Partner")
    for field, value in partner.dict(exclude_unset=True).items():
        if field == "zip_code" and not verify_zip_code(db, value):
            raise Exception("Invalid Zip Code")
        setattr(partner_found, field, value)
    db.add(partner_found)
    db.commit()
    db.refresh(partner_found)

    return partner_found


def delete_partner(db: Session, cnpj: str):
    partner = db.query(Partner).filter(Partner.cnpj == cnpj).first()
    if not partner:
        raise Exception("Not Found Partner")
    db.delete(partner)
    db.commit()
