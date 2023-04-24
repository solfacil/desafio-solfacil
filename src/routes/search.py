from typing import List

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Path,
    Query,
    Response,
    status,
)
from sqlalchemy.orm import Session

from src.database import get_db, schemas
from src.database.search import consult_partner_cnpj, search_partner
from src.utils.exceptions import response_exception
from src.utils.messages import Message

router = APIRouter()

messages = Message()
descriptions = Message("descriptions")


@router.get(
    "/{cnpj}",
    response_model=schemas.PartnerSchema,
    status_code=status.HTTP_200_OK,
    summary="Buscar parceiro por CNPJ",
    description=descriptions.get("search_partner_description"),
)
def buscar_cnpj_parceiro(
    cnpj: str = Path(..., example="01234567891234"),
    db: Session = Depends(get_db),
):
    try:
        partner = consult_partner_cnpj(db, cnpj)
        return partner.serialize()
    except Exception as e:
        return Response(content=response_exception(*e.args))


@router.get(
    "/",
    response_model=List[schemas.PartnerSchema],
    status_code=status.HTTP_200_OK,
    summary="Pesquisar parceiros",
    description=descriptions.get("search_partners_description"),
)
def pesquisar_parceiros(
    search_criteria: str = Query(..., example="Empresa Exemplo"),
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
):
    try:
        if len(search_criteria) <= 3:
            raise HTTPException(**messages.get("search_criteria_too_short"))

        partners = search_partner(db, search_criteria, skip, limit)

        if len(partners) == 0:
            raise HTTPException(
                **messages.get("no_partners_found"),
            )

        return [p.serialize() for p in partners]
    except Exception as e:
        return Response(content=response_exception(e))
