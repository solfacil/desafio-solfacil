from fastapi import FastAPI
from starlette.responses import FileResponse

# from src.database import Base, engine
from src.routes import parceiros

app = FastAPI()
favicon_path = "assets/favicon.ico"

# Base.metadata.drop_all(bind=engine)
# Base.metadata.create_all(bind=engine)


@app.get("/favicon.ico")
async def favicon():
    return FileResponse(favicon_path)


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(
    parceiros.router, tags=["Crud Parceiros"], prefix="/parceiros"
)
