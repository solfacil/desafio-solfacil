import csv

from fastapi import APIRouter, Depends, File, Response, UploadFile
from sqlalchemy.orm import Session

from src.database import get_db
from src.database.crud import update_partner
from src.utils.exceptions import response_exception
from src.utils.messages import Message
from src.utils.validations import validate_csv

router = APIRouter()

descriptions = Message("descriptions")


@router.post(
    "/partners/",
    tags=["Resposta Desafio"],
    summary="Carregar parceiros via CSV",
    description=(
        "Carregar parceiros a partir de um arquivo CSV enviado. "
        "O arquivo deve ter o seguinte formato: CNPJ, Nome, E-mail e Telefone."
        "Exemplo de conteúdo CSV:\n\n"
        "CNPJ, Razão Social, Nome Fantasia, Telefone, Email, CEP \n"
        "12.345.678/9123-45,Sol Eterno,Sol Eterno LTDA,\
(21) 98207-9901,teste@test.com,22783-115"
    ),
)
async def carregar_parceiros(
    file: UploadFile = File(
        ...,
        description=descriptions.get("upload_partners_file_description"),
    ),
    db: Session = Depends(get_db),
):
    try:
        contents = await file.read()
        decoded = contents.decode("utf-8").splitlines()
        reader = list(csv.reader(decoded))
        validated_csv = validate_csv(db, headers=reader[0], rows=reader[1:])
        partners, status = validated_csv["partners"], validated_csv["status"]
        for partner in partners:
            update_partner(db, partner.cnpj, partner, True)
        return status
    except Exception as e:
        return Response(content=response_exception(e))
