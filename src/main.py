from fastapi import FastAPI
from starlette.responses import FileResponse

from src.database import SessionLocal
from src.routes import parceiros

app = FastAPI()
favicon_path = "assets/favicon.ico"


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/favicon.ico")
async def favicon():
    return FileResponse(favicon_path)


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(
    parceiros.router, tags=["Crud Parceiros"], prefix="/parceiros"
)
