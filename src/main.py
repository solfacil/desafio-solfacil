from fastapi import FastAPI
from starlette.responses import FileResponse

from src.database import SessionLocal

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
