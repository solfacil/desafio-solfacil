from typing import List

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from src.database import get_db, schemas
from src.database.search import consult_partner_cnpj, search_partner
from src.utils.exceptions import response_exception

router = APIRouter()


@router.get("/{cnpj}", response_model=schemas.SchemaParceiro)
def buscar_cnpj_parceiro(cnpj: str, db: Session = Depends(get_db)):
    try:
        parceiro = consult_partner_cnpj(db, cnpj)
        return parceiro.serialize()
    except Exception as e:
        return Response(content=response_exception(*e.args))


@router.get("/", response_model=List[schemas.SchemaParceiro])
def pesquisar_parceiros(
    criterio: str,
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
):
    try:
        if len(criterio) <= 3:
            mensagem = (
                "Por favor, tente inserir pelo menos 4 caracteres na busca."
            )
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail={"message": mensagem},
            )
        parceiros = search_partner(db, criterio, skip, limit)
        if len(parceiros) == 0:
            mensagem = (
                "Não encontramos nenhum parceiro correspondente à sua pesquisa"
            )
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"message": mensagem},
            )
        return [p.serialize() for p in parceiros]
    except Exception as e:
        return Response(content=response_exception(e))
