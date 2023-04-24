from fastapi import FastAPI , Depends, UploadFile, File
from sqlalchemy.orm  import Session
from io import StringIO
import csv
from.model import parteners
from .controller import file_process
from .database.database import SessionLocal, engine, init_db
from .crud.crud import get_partener 

app = FastAPI()


@app.on_event("startup")
async def on_startup():
    await init_db()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/partners")
def post_csv(csv_data: UploadFile = File(...), db: Session = Depends(get_db)):
    contents = csv_data.file.read().decode("utf-8")
    csv_dict = csv.DictReader(StringIO(contents))
    data = [row for row in csv_dict]
    return  file_process.process_data(db= db,j_data = data)

@app.get("/parteners")
def post_csv(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_partener(db, skip, limit)
