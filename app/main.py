import csv, codecs
from .database import crud
from .database.connection import SessionLocal
from .dto.Customer import Customer
from .controller.customer import CustomerController
from .utils import get_logger
from fastapi import Request, status, Depends, FastAPI, HTTPException, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/templates/static"), name="static")
logger = get_logger(__name__)

def get_database():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/import-customers-from-csv/")
async def import_customers(upload_file: UploadFile = File(...), db: Session = Depends(get_database)):
    if upload_file.content_type != "text/csv":
        logger.exception("Invalid file received, only .csv files are accepted")
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail="Invalid file received, only .csv files are accepted",
        )

    csv_reader = csv.DictReader(codecs.iterdecode(upload_file.file, 'utf-8'))
    csv_line = 0
    response = {"status": "ERROR", "messages": {
            "danger": {},
            "warning": {},
            "success": {}
    }}
    for customer in csv_reader:
        csv_line += 1
        try:
            customer_controller = CustomerController(customer)
            customer_data, customer_message = await customer_controller.check_customer_data()
            if customer_message:
                response["messages"]["danger"][csv_line] = customer_message["error"] if "error" in customer_message else None
                response["messages"]["warning"][csv_line] = customer_message["warning"] if "warning" in customer_message else None

            if "customer" in customer_data:
                crud.save_customer(db, customer_data["customer"], customer_data["address"])
                response["status"] = "SUCCESS"
                response["messages"]["success"][csv_line] = f'Customer {customer["Razão Social"]} saved'

        except Exception as error:
            response["status"] = "ERROR"
            response["messages"]['danger'][csv_line] = str(error)
            logger.exception(str(error))

    upload_file.file.close()
    db.expunge_all()
    logger.info(f'Processed {csv_line} lines in file.')

    raise HTTPException(status_code=status.HTTP_200_OK, detail=response)

@app.get("/list-customers/", response_model=list[Customer])
def list_customers(skip: int = 0, limit: int = 100, db: Session = Depends(get_database)):
    customers = crud.get_customers(db, skip=skip, limit=limit)
    return customers

@app.get("/search-customer/{client_id}", response_model=Customer)
def get_customer(client_id: int, db: Session = Depends(get_database)):
    customer = crud.get_customer_by_id(db, customer_id=client_id)
    if customer is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found")
    return customer
