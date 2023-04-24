from sqlalchemy.orm import Session
from sqlalchemy import update
from ..model import parteners

def get_partener(db: Session, skip: int = 0, limit: int = 100):
    return db.query(parteners.Partener).offset(skip).limit(limit).all()

def update_partener(db: Session, data: list[parteners.Partener]):
    added_email_list = []
    for partener in data:
        existing_partener = db.query(parteners.Partener).filter_by(cnpj=partener.cnpj).first()
        if existing_partener:
            # Update existing partener with new data
            existing_partener.razao_social = partener.razao_social
            existing_partener.name = partener.name
            existing_partener.phone_number = partener.phone_number
            existing_partener.email = partener.email
            existing_partener.address = partener.address
            db.merge(existing_partener)
        else:
            added_email_list.append(str(partener.email))
            db.add(partener)
    db.commit()
    return added_email_list