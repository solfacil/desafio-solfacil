from typing import List

from fastapi import APIRouter, Depends, HTTPException, Query, Response, status
from sqlalchemy.orm import Session
from validate_docbr import CNPJ

from src.database import get_db, schemas
from src.database.crud import (
    create_partner,
    delete_partner,
    list_partners,
    update_partner,
)
from src.utils.exceptions import response_exception
from src.utils.messages import Message

router = APIRouter()
messages = Message()
descriptions = Message("descriptions")


@router.get(
    "/",
    response_model=List[schemas.PartnerSchema],
    status_code=status.HTTP_200_OK,
    tags=["Resposta Desafio"],
    summary="Listar parceiros",
    description=descriptions.get("list_partners_description"),
)
def listar_parceiros(
    skip: int = Query(
        0, description="Número de registros para pular na listagem", example=0
    ),
    limit: int = Query(
        10,
        description="Limite de registros a serem retornados na listagem",
        example=10,
    ),
    db: Session = Depends(get_db),
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
    summary="Criar parceiro",
    description=descriptions.get("create_partner_description"),
)
def criar_parceiro(
    partner: schemas.PartnerJsonSchema, db: Session = Depends(get_db)
):
    try:
        new_partner, status_message = create_partner(db, partner)
        if status_message:
            return new_partner.serialize()
    except Exception as e:
        Response(content=response_exception(*e.args))


@router.put(
    "/{cnpj}",
    response_model=schemas.PartnerSchema,
    status_code=status.HTTP_200_OK,
    summary="Atualizar parceiro",
    description=descriptions.get("update_partner_description"),
)
def atualizar_parceiro(
    cnpj: str,
    partner: schemas.PartnerUpdateSchema,
    db: Session = Depends(get_db),
):
    try:
        updated_partner, status_message = update_partner(db, cnpj, partner)
        if status_message:
            return updated_partner.serialize()
    except Exception as e:
        Response(content=response_exception(*e.args))


@router.delete(
    "/{cnpj}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Deletar parceiro",
    description=descriptions.get("delete_partner_description"),
)
def deletar_parceiro(cnpj: str, db: Session = Depends(get_db)):
    try:
        if not CNPJ().validate(cnpj):
            raise HTTPException(**messages.get("cnpj_invalid"))
        cnpj = "".join(filter(str.isdigit, cnpj))
        delete_partner(db, cnpj)
    except Exception as e:
        Response(content=response_exception(e))
