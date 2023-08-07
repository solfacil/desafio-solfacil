from typing import Optional
from pydantic import BaseModel
from sqlalchemy.orm import Session
from pycpfcnpj import cpfcnpj
from email_validator import validate_email, EmailNotValidError

from app.database.models import adresses, customers
from app.internal.schemas.address import Address


class Customer(BaseModel):
    class Config:
        from_attributes = True

    cliente_id: Optional[int] = None
    razao_social: str
    email: Optional[str] = None
    nome_fantasia: Optional[str] = None
    telefone: Optional[str] = None
    cpf: Optional[str] = None
    cnpj: Optional[str] = None
    cep: Optional[int] = None
    tipo_pessoa: str
    enderecos: list[Address] = []


def check_customer_data(customer: dict):
    customer_data = {}
    customer_messages = {}
    if any(customer.values()) == True and "CNPJ" in customer and "Razão Social" in customer:
        if cpfcnpj.validate(customer["CNPJ"]) == True and customer["Razão Social"] != "":
            customer_identify = ''.join(
                identify for identify in customer["CNPJ"] if identify.isdigit())
            customer_phone = ''.join(
                phone for phone in customer["Telefone"] if phone.isdigit())
            cep = ''.join(digit_cep for digit_cep in customer["CEP"] if digit_cep.isdigit(
            )) if customer["CEP"] != '' else None
            email = None
            customer_pj = True
            customer_person_type = "PJ"

            try:
                customer_email = validate_email(
                    customer["Email"], check_deliverability=False)
                email = customer_email.normalized
            except EmailNotValidError as error:
                customer_messages["warning"] = f'Customer email {customer["Email"]} is invalid'

            if len(customer_identify) == 11:
                customer_pj = False
                customer_person_type = "PF"

            cnpj = customer["CNPJ"] if customer_pj == True else None
            cpf = customer["CNPJ"] if customer_pj == False else None
            razao_social = customer["Razão Social"]
            telefone = customer["Telefone"] if len(
                customer_phone) == 10 or len(customer_phone) == 11 else None
            nome_fantasia = customer["Nome Fantasia"]

            customer_data["customer"] = {"email": email, "razao_social": razao_social, "nome_fantasia": nome_fantasia,
                                         "telefone": telefone, "cpf": cpf, "cnpj": cnpj, "cep": cep, "tipo_pessoa": customer_person_type}
        else:
            customer_messages["error"] = 'Customer identify "CPF/CNPJ" or "Razão Social" is invalid'
    else:
        customer_messages["error"] = f'Invalid customer data'

    return customer_data, customer_messages


def get_customer_by_id(db: Session, customer_id: int):
    return db.query(customers.Customers).filter(customers.Customers.cliente_id == customer_id).first()


def get_customer_by_name(db: Session, customer_name: str):
    return db.query(customers.Customers).filter(customers.Customers.razao_social == customer_name).first()


def get_customer_address_by_cep(db: Session, cep: str):
    return db.query(adresses.Adresses).filter(adresses.Adresses.cep == cep).first()


def get_customers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(customers.Customers).join(adresses.Adresses).offset(skip).limit(limit).all()


def save_customer(db: Session, customer: dict):
    db_customer = customers.Customers(**customer)
    customer_data = get_customer_by_name(db, customer["razao_social"])
    if customer_data != None:
        db_customer.cliente_id = customer_data.cliente_id
        db.merge(db_customer)
        db.commit()
    else:
        db.add(db_customer)
        db.commit()

    return db_customer
