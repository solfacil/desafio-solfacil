from fastapi import APIRouter

from src.database import schemas

router = APIRouter()


@router.get("/", response_model=list[schemas.SchemaParceiro])
def get_parceiros():
    return []
