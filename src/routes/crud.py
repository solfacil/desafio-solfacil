from typing import List

from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from src.database import get_db, schemas
from src.database.crud import (
    create_partner,
    delete_partner,
    list_partners,
    update_partner,
)
from src.utils.exceptions import response_exception

router = APIRouter()


@router.get(
    "/",
    response_model=List[schemas.PartnerSchema],
    status_code=status.HTTP_200_OK,
    tags=["Resposta Desafio"],
)
def listar_parceiros(
    skip: int = 0, limit: int = 10, db: Session = Depends(get_db)
):
    try:
        partners = list_partners(db, skip, limit)
        return [p.serialize() for p in partners]
    except Exception as e:
        return Response(content=response_exception(*e.args))


@router.post(
    "/",
    response_model=schemas.PartnerSchema,
    status_code=status.HTTP_201_CREATED,
)
def criar_parceiro(
    partner: schemas.PartnerJsonSchema, db: Session = Depends(get_db)
):
    try:
        new_partner = create_partner(db, partner)
        return new_partner.serialize()
    except Exception as e:
        Response(content=response_exception(*e.args))


@router.put(
    "/{cnpj}",
    response_model=schemas.PartnerSchema,
    status_code=status.HTTP_200_OK,
)
def atualizar_parceiro(
    cnpj: str,
    partner: schemas.PartnerUpdateSchema,
    db: Session = Depends(get_db),
):
    try:
        updated_partner = update_partner(db, cnpj, partner)
        return updated_partner.serialize()
    except Exception as e:
        Response(content=response_exception(*e.args))


@router.delete("/{cnpj}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_parceiro(cnpj: str, db: Session = Depends(get_db)):
    try:
        delete_partner(db, cnpj)
    except Exception as e:
        Response(content=response_exception(*e.args))
