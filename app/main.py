from fastapi import Request, status, Depends, FastAPI, HTTPException, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database.connection import SessionLocal
import app.internal.schemas.customer as Customer
import app.internal.schemas.address as Address
import app.pkg.utils as Utils

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/templates/static"), name="static")
logger = Utils.get_logger(__name__)


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

    csv_line = 0
    response = {"status": "ERROR", "messages": {
        "danger": {},
        "warning": {},
        "success": {}
    }}
    try:
        csv_reader = Utils.read_csv_file(upload_file.file)
        for customer in csv_reader:
            csv_line += 1
            customer = {key.strip(): value for key, value in customer.items()}
            customer_data, customer_message = Customer.check_customer_data(
                customer)

            if "error" in customer_message:
                response["messages"]["danger"][csv_line] = customer_message["error"]
            if "warning" in customer_message:
                response["messages"]["warning"][csv_line] = customer_message["warning"]

            if "customer" in customer_data and "error" not in customer_message:
                Customer.save_customer(db, customer_data["customer"])
                response["status"] = "SUCCESS"
                response["messages"]["success"][csv_line] = f'Customer {customer["Razão Social"]} saved'
                if customer_data["customer"]['cep'] != None:
                    address_data = await Address.get_address_from_external_cep_api(customer_data["customer"]['cep'])
                    if address_data:
                        Address.save_address(db, address_data)

    except Exception as error:
        response["status"] = "ERROR"
        response["messages"]['danger'][csv_line] = str(error)
        logger.exception(str(error))

    upload_file.file.close()
    db.expunge_all()
    logger.info(f'Processed {csv_line} lines in file.')

    raise HTTPException(status_code=status.HTTP_200_OK, detail=response)


@app.get("/v1/partners/customers/")
async def list_customers(skip: int = 0, limit: int = 100, db: Session = Depends(get_database)):
    try:
        customers = Customer.get_customers(db, skip=skip, limit=limit)
        if customers is None:
            raise HTTPException(status_code=status.HTTP_200_OK,
                                detail="Customers not found")
        return customers
    except Exception as error:
        logger.exception(str(error))
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error))


@app.get("/v1/partners/customers/{client_id}")
async def get_customer(client_id: int, db: Session = Depends(get_database)):
    try:
        customer = Customer.get_customer_by_id(db, customer_id=client_id)
        if customer is None:
            raise HTTPException(
                status_code=status.HTTP_200_OK, detail="Customer not found")
        return customer
    except Exception as error:
        logger.exception(str(error))
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error))
