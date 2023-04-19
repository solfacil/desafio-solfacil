from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_parceiros():
    return {"message": "Rota Funcionando!"}
