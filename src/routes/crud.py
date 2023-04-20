from typing import List

from fastapi import APIRouter, Depends, Response, status
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from src.database import get_db, schemas
from src.database.crud import (
    atualizar_parceiro,
    consultar_parceiros,
    criar_parceiro,
    deletar_parceiro,
)
from src.utils import response_exception

router = APIRouter()


@router.get("/", response_model=List[schemas.SchemaParceiro])
def get_parceiros(
    skip: int = 0, limit: int = 10, db: Session = Depends(get_db)
):
    try:
        parceiros = consultar_parceiros(db, skip, limit)
        return jsonable_encoder(parceiros)
    except Exception as e:
        return Response(content=response_exception(*e.args))


@router.post(
    "/",
    response_model=schemas.SchemaParceiro,
    status_code=status.HTTP_201_CREATED,
)
def post_parceiro(
    parceiro: schemas.SchemaJsonParceiro, db: Session = Depends(get_db)
):
    try:
        novo_parceiro = criar_parceiro(db, parceiro)
        print(novo_parceiro)
        return jsonable_encoder(novo_parceiro)
    except Exception as e:
        Response(content=response_exception(*e.args))


@router.put(
    "/{cnpj}",
    response_model=schemas.SchemaParceiro,
)
def put_parceiro(
    cnpj: str,
    parceiro: schemas.SchemaJsonParceiro,
    db: Session = Depends(get_db),
):
    try:
        db_parceiro = atualizar_parceiro(db, cnpj, parceiro)
        return jsonable_encoder(db_parceiro)
    except Exception as e:
        Response(content=response_exception(*e.args))


@router.delete("/{cnpj}", status_code=status.HTTP_204_NO_CONTENT)
def delete_parceiro(cnpj: str, db: Session = Depends(get_db)):
    try:
        deletar_parceiro(db, cnpj)
    except Exception as e:
        Response(content=response_exception(*e.args))
