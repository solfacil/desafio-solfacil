import csv

from fastapi import APIRouter, Depends, File, Response, UploadFile
from sqlalchemy.orm import Session

from src.database import get_db
from src.utils.exceptions import response_exception
from src.utils.proc_parceiros import processar

router = APIRouter()


# Rota para receber o arquivo e salvar no banco de dados
@router.post("/parceiros/", tags=["Resposta Desafio"])
async def upload_parceiros(
    file: UploadFile = File(...), db: Session = Depends(get_db)
):
    try:
        contents = await file.read()
        decoded = contents.decode("utf-8").splitlines()
        reader = list(csv.reader(decoded))
        status_upload = processar(db, headers=reader[0], rows=reader[1:])
        return status_upload
    except Exception as e:
        return Response(content=response_exception(e))
