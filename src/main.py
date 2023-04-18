from fastapi import FastAPI
from starlette.responses import FileResponse

app = FastAPI()
favicon_path = "assets/favicon.ico"


@app.get("/favicon.ico")
async def favicon():
    return FileResponse(favicon_path)


@app.get("/")
async def root():
    return {"message": "Hello World"}
