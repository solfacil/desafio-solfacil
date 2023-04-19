from typing import List

from fastapi import APIRouter, Depends, Response, status
from fastapi.encoders import jsonable_encoder

from src.database import get_db, schemas
from src.database.crud import consultar_parceiros, criar_parceiro
from src.utils import response_exception

router = APIRouter()


@router.get("/", response_model=List[schemas.SchemaParceiro])
def get_parceiros(skip: int = 0, limit: int = 10, db=Depends(get_db)):
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
def post_parceiro(parceiro: schemas.SchemaCriacaoParceiro, db=Depends(get_db)):
    try:
        novo_parceiro = criar_parceiro(db, parceiro)
        print(novo_parceiro)
        return jsonable_encoder(novo_parceiro)
    except Exception as e:
        Response(content=response_exception(*e.args))
