from platform import python_version

from fastapi import FastAPI
from starlette.responses import FileResponse

from src.routes import parceiros

app = FastAPI()
favicon_path = "assets/favicon.ico"


@app.get("/favicon.ico")
async def favicon():
    return FileResponse(favicon_path)  # pragma: no cover


@app.get("/")
async def root():
    return {"python_version": python_version()}


app.include_router(
    parceiros.router, tags=["Crud Parceiros"], prefix="/parceiros"
)
