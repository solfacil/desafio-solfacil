from fastapi import FastAPI

from .domains.parceiros.repositories.sqlalchemy import models
from .domains.parceiros.repositories.sqlalchemy.database import engine
from src.routes_v1 import router

models.Base.metadata.create_all(bind=engine)

# Criando uma instância do FastAPI
app = FastAPI(
    title="Atualização em lote de Parceiros",
    description="Endpoints para listagem e atualização de parceiros em lote através de arquivo csv",
)

app.include_router(router, prefix="/parceiros")
