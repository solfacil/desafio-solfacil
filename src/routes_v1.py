from fastapi import APIRouter, Depends, File, UploadFile
from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from .domains.parceiros.repositories.sqlalchemy import crud, schemas
from .domains.parceiros.repositories.sqlalchemy.database import SessionLocal
from .domains.parceiros.repositories.sqlalchemy.models import Parceiro
from .utils.cep_search import define_parceiro_location
from .utils.read_file import read_csv
from .utils.validations import is_cnpj_valid, is_email_valid
from .utils.write_notification import send_email
from typing import List

router = APIRouter()


# Dependencia
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get(
    "/listagem/",
    response_model=List[schemas.Parceiro],
    name="Listagem de parceiros",
    tags=["api v1 - listagem de parceiros"],
)
async def fetch_all_parceiros(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    parceiros = crud.get_parceiros(db, skip=skip, limit=limit)
    return parceiros


@router.post(
    "/upload_csv/",
    name="Upload de arquivo csv de parceiros",
    tags=["api v1 - atualização de parceiros"],
)
async def upload_csv(file: UploadFile = File(...), db: Session = Depends(get_db)):
    if not file.size:
        return {"message": "Arquivo csv não encontrado."}

    # Read the uploaded CSV file
    rows = await read_csv(file)
    # Skip the header
    next(rows)

    # Initialize variables
    errors = []
    row_count = 0

    for row in rows:
        # Increments the row_count for each iteration
        row_count += 1
        # Extract the data from the CSV row
        parceiro = {
            "cnpj": row["CNPJ"],
            "razao_social": row["Razão Social"],
            "nome_fantasia": row["Nome Fantasia"],
            "telefone": row["Telefone"],
            "email": row["Email"],
            "cep": row["CEP"],
            "cidade": None,
            "estado": None,
        }

        # Collect location information based on CEP
        if parceiro["cep"]:
            region = define_parceiro_location(parceiro["cep"])
            parceiro.update({"cidade": region["cidade"], "estado": region["estado"]})

        # Validate if CNPJ is valid. If is valid it queries the database
        # to check if Parceiro already exists, it it exists sets
        # parceiro_already_exists to Parceiro Object
        if is_cnpj_valid(parceiro["cnpj"]):
            parceiro_exists = (
                db.query(Parceiro).filter(Parceiro.cnpj == parceiro["cnpj"]).first()
            )
        else:
            errors.append(
                f'Erro na linha {row_count}. CNPJ {parceiro["cnpj"]} inválido.'
            )
            parceiro_exists = None

        # Validate if Email is valid. If not sends a message to the admin
        # to contact Parceiro
        if not is_email_valid(parceiro["email"]):
            errors.append(
                f'Erro na linha {row_count}. Email inválido! Contate o parceiro e valide a informação {parceiro["telefone"]}'  # noqa
            )

        if not parceiro_exists:
            try:
                # Creates a new Parceiro
                parceiro_created = crud.create_parceiro(db, parceiro)
                # Sends an welcome message if Parceiro is created
                if parceiro_created:
                    send_email(parceiro)

            except UniqueViolation as err:
                db.rollback()
                print(err)
            except IntegrityError as err:
                db.rollback()
                print(err)

        else:
            # Uptade Parceiro data
            crud.update_parceiro(db, parceiro_exists, parceiro)

    return {"message": "CSV file uploaded successfully.", "errors": errors}
