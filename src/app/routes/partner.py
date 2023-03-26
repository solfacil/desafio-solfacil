import csv
import io
import json
from typing import Any

import definitions
from database import DB, Session
from fastapi import APIRouter, Depends, Response, UploadFile, status
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy_future import paginate
from loguru import logger
from models import CreatePartner, ListPartner, PartnerAddress, PartnerContact, UploadCSVReturn
from pydantic import ValidationError
from schemas.Partner import Partner as DBPartner
from schemas.PartnerAddress import PartnerAddress as DBPartnerAddress
from schemas.PartnerContact import PartnerContact as DBPartnerContact
from send_email import send_email
from sqlalchemy import select

# --------------------------------------------------

router = APIRouter(prefix='/partner', tags=["partner"])

# --------------------------------------------------


def generate_partner_info(csv_reader: csv.DictReader) -> tuple[list[CreatePartner], list[Any]]:
    # will iter over key and values, trying to match any value in the list with the CSV
    # so it should accept 'Razão Social' or 'razão social' on column name, both would go to
    # our pydantic model @ razao_social field
    partner_fields = {
        'cnpj': ['CNPJ', 'cnpj'],
        'razao_social': ['Razão Social', 'razão social'],
        'nome_fantasia': ['Nome Fantasia', 'nome fantasia']
    }  # yapf: disable
    partner_address_fields = {
        'cep': ['CEP', 'cep']
    }  # yapf: disable
    partner_contact_fields = {
        'telefone': ['Telefone', 'telefone'],
        'email': ['email', 'e-mail']
    }  # yapf: disable

    # --------------------------------------------------

    def normalize_row_keys(row: dict):
        new_row = {}
        for k, v in row.items():
            new_name = str(k).strip().lower()
            new_row[new_name] = v
        return new_row

    def build(row: dict, input: dict):
        output = {}
        for field, possible_names in input.items():
            for name in possible_names:
                # if (value := row.get(name, None)) is not None: break
                try:
                    value = row[name]
                except KeyError:
                    continue
                break
            else:
                raise KeyError(f"Couldn't find any value for '{field}' with '{possible_names}'. Available names are: '{list(row.keys())}'")

            output[field] = value
            logger.debug(f"Found '{field}'='{value}' with '{name}'")
        return output

    # --------------------------------------------------

    loaded = []
    errors = []
    for row in csv_reader:
        logger.debug('=' * 60)
        row = normalize_row_keys(row)

        try:
            logger.debug("Building partner")
            partner_values = build(row, partner_fields)

            # --------------------------------------------------

            logger.debug("Building contact information")
            partner_contact_values = build(row, partner_contact_fields)

            # --------------------------------------------------

            logger.debug("Building address information")
            partner_address_values = build(row, partner_address_fields)

        except KeyError as e:
            logger.warning(e)
            errors.extend([{'KeyError': ', '.join(e.args)}])
            continue

        # --------------------------------------------------

        try:
            data = {**partner_values, 'address': partner_address_values, 'contact': partner_contact_values}
            logger.debug(f"Creating partner with data: {data}")
            partner = CreatePartner(**data)
        except ValidationError as e:
            logger.warning(e)
            errors.extend(json.loads(e.json()))
            continue

        loaded.append(partner)

    # --------------------------------------------------

    logger.debug(f"{errors = }")
    logger.debug(f"{loaded = }")
    return loaded, errors


def create_or_update_partner(db: Session, partner_data: CreatePartner):
    """Get the partner info from Pydantic Models, then load into DB, updating fields if needed"""
    partner_contact: PartnerContact = partner_data.contact
    partner_address: PartnerAddress = partner_data.address

    # --------------------------------------------------
    # create the partner
    data = partner_data.dict()
    data.pop('address')
    data.pop('contact')
    partner_in_db, is_new = DBPartner.create_or_update(db, data, cnpj=partner_data.cnpj)

    # --------------------------------------------------
    try:
        # create the contact
        data = {'partner_id': partner_in_db.id, **partner_contact.dict()}
        DBPartnerContact.create_or_update(db, data, partner_id=partner_in_db.id)

        # --------------------------------------------------
        data = {'partner_id': partner_in_db.id, **partner_address.dict()}
        DBPartnerAddress.create_or_update(db, data, partner_id=partner_in_db.id)

    except Exception as e:
        logger.critical(f"Failed creating partner: {partner_data}, error '{e}', ")
        db.rollback()
        db.delete(partner_in_db)
        db.commit()
        raise

    if not definitions.EMAIL_ENABLED:
        logger.debug("E-mails to new partners are disabled! Enable setting environment EMAIL_ENABLED='1'")
    elif is_new and definitions.EMAIL_ENABLED:
        data = {
            'to': partner_in_db.contact.email,
            'html_body': f"You are now in our systems {partner_in_db.razao_social}!",
            'title': "Howdy Partner!",
            'bcc': "my_qa@company.com",
            **definitions.email_infos
        }
        send_email(**data)

    db.commit()
    return


@router.post("/insert_update_by_csv", status_code=status.HTTP_202_ACCEPTED)
async def upload_csv(file: UploadFile, db: Session = Depends(DB.get_db)) -> UploadCSVReturn:
    """"Receives a CSV file, then bulk insert/update our database with data from the CSV, using CNPJ as filter"""
    contents = await file.read()
    csv_io = io.StringIO(contents.decode())

    csv_reader = csv.DictReader(csv_io)

    # --------------------------------------------------
    # filter and generate pydantic models, save the errors if any
    partners, errors = generate_partner_info(csv_reader)

    # --------------------------------------------------
    # loads the pydantic models into db
    for partner in partners:
        create_or_update_partner(db, partner)

    # --------------------------------------------------
    return {'loaded': partners, 'errors': errors}


# --------------------------------------------------


@router.get("/list", response_model=Page[ListPartner])
async def list_partners(db: Session = Depends(DB.get_db)):
    return paginate(db, select(DBPartner))


# --------------------------------------------------


@router.post("/create", response_model=ListPartner, status_code=status.HTTP_201_CREATED)
async def create_partner(new_partner: CreatePartner, db: Session = Depends(DB.get_db)):
    in_db_partner = db.query(DBPartner).filter_by(cnpj=new_partner.cnpj).first()
    if in_db_partner:
        return Response(f"Partner with cnpj '{new_partner.cnpj}' already exists", status.HTTP_302_FOUND)

    new_partner_dict = new_partner.dict().copy()
    new_partner_dict.pop('address')
    new_partner_dict.pop('contact')
    new_db_partner = DBPartner(**new_partner_dict)
    db.add(new_db_partner)
    db.commit()
    db.refresh(new_db_partner)
    try:
        db.add(DBPartnerAddress(**{'partner_id': new_db_partner.id, **new_partner.address.dict()}))
        db.add(DBPartnerContact(**{'partner_id': new_db_partner.id, **new_partner.contact.dict()}))
    except Exception as e:
        logger.warning(f"Error '{e}' while adding new partner")
        db.rollback()
        db.delete(new_db_partner)
        db.commit()
        raise

    db.commit()

    db.refresh(new_db_partner)

    if not definitions.EMAIL_ENABLED:
        logger.debug("E-mails to new partners are disabled! Enable setting environment EMAIL_ENABLED='1'")
    else:
        data = {
            'to': new_partner.contact.email,
            'html_body': f"You are now in our systems {new_partner.razao_social}!",
            'title': "Howdy Partner!",
            'bcc': "my_qa@company.com",
            **definitions.email_infos
        }
        send_email(**data)

    return new_db_partner
