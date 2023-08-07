import csv
import codecs
from fastapi import Request, status, Depends, FastAPI, HTTPException, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from .database.connection import SessionLocal
from .internal.schemas.customer import Customer, check_customer_data, save_customer, get_customers, get_customer_by_id
from .internal.schemas.address import get_address_from_external_cep_api, save_address
from .pkg.utils import get_logger

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


@app.post("/v1/partners/customers/")
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
        customer = {key.strip(): value for key, value in customer.items()}
        try:
            customer_data, customer_message = check_customer_data(customer)
            if customer_message:
                response["messages"]["danger"][csv_line] = customer_message["error"] if "error" in customer_message else None
                response["messages"]["warning"][csv_line] = customer_message["warning"] if "warning" in customer_message else None

            if "customer" in customer_data:
                save_customer(db, customer_data["customer"])
                response["status"] = "SUCCESS"
                response["messages"]["success"][csv_line] = f'Customer {customer["Razão Social"]} saved'
                if customer_data["customer"]['cep'] != None:
                    address_data = await get_address_from_external_cep_api(customer_data["customer"]['cep'])
                    if address_data:
                        save_address(db, address_data)

        except Exception as error:
            response["status"] = "ERROR"
            response["messages"]['danger'][csv_line] = str(error)
            logger.exception(str(error))

    upload_file.file.close()
    db.expunge_all()
    logger.info(f'Processed {csv_line} lines in file.')

    raise HTTPException(status_code=status.HTTP_200_OK, detail=response)


@app.get("/v1/partners/customers/", response_model=list[Customer])
async def list_customers(skip: int = 0, limit: int = 100, db: Session = Depends(get_database)):
    try:
        customers = await get_customers(db, skip=skip, limit=limit)
        if customers is None:
            raise HTTPException(status_code=status.HTTP_200_OK,
                                detail="Customers not found")
        else:
            raise HTTPException(
                status_code=status.HTTP_200_OK, detail=customers)
    except Exception as error:
        logger.exception(str(error))
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error))


@app.get("/v1/partners/customers/{client_id}", response_model=Customer)
async def get_customer(client_id: int, db: Session = Depends(get_database)):
    try:
        customer = await get_customer_by_id(db, customer_id=client_id)
        if customer is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found")
        else:
            raise HTTPException(
                status_code=status.HTTP_200_OK, detail=customer)
    except Exception as error:
        logger.exception(str(error))
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error))
