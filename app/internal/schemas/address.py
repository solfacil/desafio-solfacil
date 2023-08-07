from typing import Optional
from pydantic import BaseModel
from sqlalchemy.orm import Session
from ...database.models.adresses import Adresses
from ...pkg.utils import call_external_cep_api


class Address(BaseModel):
    class Config:
        from_attributes = True

    endereco_id: Optional[int] = None
    cep: Optional[str] = None
    logradouro: Optional[str] = None
    complemento: Optional[str] = None
    bairro: Optional[str] = None
    localidade: Optional[str] = None
    uf: Optional[str] = None
    ibge: Optional[str] = None


async def get_address_from_external_cep_api(cep: int):
    address_data = None
    if len(cep) == 8:
        address_search = await call_external_cep_api(cep)
        if address_search:
            address_data = {"cep": cep, "logradouro": address_search['logradouro'], "complemento": address_search['complemento'],
                            "bairro": address_search['bairro'], "localidade": address_search['localidade'], "uf": address_search['uf'], "ibge": address_search['ibge']}

    return address_data


def get_address_by_cep(db: Session, cep: int):
    return db.query(Adresses).filter(Adresses.cep == cep).first()


def save_address(db: Session, address: dict):
    db_address = Adresses(**address)
    address = get_address_by_cep(db, db_address.cep)
    if address != None:
        db_address.endereco_id = address.endereco_id
        db.merge(db_address)
        db.commit()
    else:
        db.add(db_address)
        db.commit()

    db.refresh(db_address)
    return db_address


def delete_customer_address(db: Session, address: dict) -> None:
    db.delete(address)
    db.commit()
