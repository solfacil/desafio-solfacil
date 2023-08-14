from typing import Optional, List

from fastapi import APIRouter
from fastapi import status, Depends, HTTPException, UploadFile, File, Path, Query

from sqlalchemy.orm import Session

from app.database.connection import get_database
import app.pkg.utils as Utils
import app.internal.schemas.customer as CustomerSchema
import app.internal.schemas.address as AddressSchema

logger = Utils.get_logger(__name__)

router = APIRouter()


@router.post('/customers', summary='Import customers', description='Import customers to partners from csv file')
async def import_customers_from_csv(upload_file: UploadFile = File(default=None, title='Import customers from partners', description='Use to send a csv file with a list of customers from partners to import'), db: Session = Depends(get_database)):
    if upload_file == None or upload_file.content_type != "text/csv":
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
            customer_data, customer_message = CustomerSchema.check_customer_data(
                customer)

            if "error" in customer_message:
                response["messages"]["danger"][csv_line] = customer_message["error"]
            if "warning" in customer_message:
                response["messages"]["warning"][csv_line] = customer_message["warning"]

            if "customer" in customer_data and "error" not in customer_message:
                CustomerSchema.save_customer(db, customer_data["customer"])
                response["status"] = "SUCCESS"
                response["messages"]["success"][csv_line] = f'Customer {customer["Razão Social"]} saved'
                if customer_data["customer"]['cep'] != None:
                    address_data = await AddressSchema.get_address_from_external_cep_api(customer_data["customer"]['cep'])
                    if address_data:
                        AddressSchema.save_address(db, address_data)

    except Exception as error:
        response["status"] = "ERROR"
        response["messages"]['danger'][csv_line] = str(error)
        logger.exception(str(error))

    upload_file.file.close()
    db.expunge_all()
    logger.info(f'Processed {csv_line} lines in file.')

    raise HTTPException(status_code=status.HTTP_201_CREATED, detail=response)


@router.get('/customers', summary='Get customers', description='Get a paginated list of customers', response_model=List[Optional[CustomerSchema.Customer]])
async def list_customers(skip: int = Query(default=0, title='Row to start', description='Specify which row to start retrieving from'), limit: int = Query(default=100, title='Number of rows', description='Specify the number of rows from the output', gt=0), db: Session = Depends(get_database)):
    customers = CustomerSchema.get_customers(db, skip=skip, limit=limit)
    if customers is None:
        raise HTTPException(status_code=status.HTTP_200_OK,
                            detail="Customers not found")
    return customers


@router.get('/customers/{customer_id}', summary='Get customer', description='Get a specific customer from id', response_model=Optional[CustomerSchema.Customer])
async def get_customer(customer_id: int = Path(title='Data from customer', description='This method return data of customer from partners', gt=0), db: Session = Depends(get_database)):
    customer = CustomerSchema.get_customer_by_id(db, customer_id=customer_id)
    if customer is None:
        raise HTTPException(
            status_code=status.HTTP_200_OK, detail="Customer not found")
    return customer
