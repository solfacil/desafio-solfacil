import csv

from fastapi import APIRouter, Depends, File, Response, UploadFile
from sqlalchemy.orm import Session

from src.database import get_db
from src.database.crud import update_partner
from src.utils.exceptions import response_exception
from src.utils.validations import validate_csv

router = APIRouter()


@router.post("/partners/", tags=["Resposta Desafio"])
async def carregar_parceiros(
    file: UploadFile = File(...), db: Session = Depends(get_db)
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
