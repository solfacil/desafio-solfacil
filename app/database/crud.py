from sqlalchemy.orm import Session

from ..models.Models import Customers, Adresses
from ..dto.Customer import CustomerData
from ..dto.Address import AddressData

def get_customer_by_id(db: Session, customer_id: int):
    return db.query(Customers).filter(Customers.cliente_id == customer_id).first()

def get_customer_by_name(db: Session, customer_name: str):
    return db.query(Customers).filter(Customers.razao_social == customer_name).first()

def get_customers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Customers).offset(skip).limit(limit).all()

def save_customer(db: Session, customer: CustomerData, address: dict):
    db_customer = Customers(email=customer.email, razao_social=customer.razao_social, nome_fantasia=customer.nome_fantasia, telefone=customer.telefone, cpf=customer.cpf, cnpj=customer.cnpj)
    customer_data = get_customer_by_name(db, customer.razao_social)
    if customer_data != None:
        db_customer.cliente_id = customer_data.cliente_id
        db.merge(db_customer)
        db.commit()
    else:
        db.add(db_customer)
        db.commit()
    
    if address:
        address_data = AddressData(cep=address['cep'], logradouro=address['logradouro'], complemento=address['complemento'], bairro=address['bairro'], localidade=address['localidade'], uf=address['uf'], ibge=address['ibge'])
        save_customer_address(db, address_data, db_customer.cliente_id)

    return db_customer

def get_customer_address_by_cep(db: Session, cep: str, customer_id: int):
    return db.query(Adresses).filter(Adresses.cep == cep, Adresses.cliente_id == customer_id).first()

def get_customer_address(db: Session, customer_id: int):
    return db.query(Adresses).filter(Adresses.cliente_id == customer_id).first()

def save_customer_address(db: Session, address: AddressData, customer_id: int):
    db_address = Adresses(**address.dict(), cliente_id=customer_id)
    customer_address = get_customer_address(db, customer_id)
    if customer_address:
        if customer_address.cep != db_address.cep:
            delete_customer_address(db, customer_address)
        else:
            return db_address

    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address

def delete_customer_address(db: Session, address: dict) -> None:
    db.delete(address)
    db.commit()