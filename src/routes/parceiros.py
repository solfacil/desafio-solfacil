from fastapi import APIRouter, Depends, status

from src.database import get_db, schemas
from src.database.crud import criar_parceiro

router = APIRouter()


@router.get("/", response_model=list[schemas.SchemaParceiro])
def consultas_parceiros():
    return []


@router.post(
    "/",
    response_model=schemas.SchemaParceiro,
    status_code=status.HTTP_201_CREATED,
)
def novo_parceiro(parceiro: schemas.SchemaCriacaoParceiro, db=Depends(get_db)):
    novo_parceiro = criar_parceiro(db, parceiro)
    return {
        "id_parceiro": novo_parceiro.id_parceiro,
        "cnpj": novo_parceiro.cnpj,
        "cep": novo_parceiro.cep,
        "data_atualizacao": novo_parceiro.data_atualizacao,
    }
