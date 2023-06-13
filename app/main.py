# app/main.py
from app import  api, database
from fastapi import FastAPI, File, UploadFile

app = FastAPI(title="FastAPI, Docker, and Traefik")

@app.get("/partners")
def get():
    result = database.get_all()
    return result


@app.post("/upload")
def upload(file: UploadFile = File(...)):
    result = api.upload_csv(file)
    return result
