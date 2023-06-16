import httpx
from ..dto.Customer import CustomerData
from ..utils import get_logger
from pycpfcnpj import cpfcnpj
from email_validator import validate_email, EmailNotValidError

class CustomerController:

    customer = None
    logger = get_logger(__name__)

    def __init__(self, customer: dict) -> None:
        self.customer = {key.strip(): value for key, value in customer.items()}

    async def check_customer_data(self):
        customer_data = {}
        customer_messages = {}
        if any(self.customer.values()) == True and "CNPJ" in self.customer and "Razão Social" in self.customer:
            if cpfcnpj.validate(self.customer["CNPJ"]) == True and self.customer["Razão Social"] != "":
                customer_idenfity = ''.join(identify for identify in self.customer["CNPJ"] if identify.isdigit())
                customer_phone = ''.join(phone for phone in self.customer["Telefone"] if phone.isdigit())
                customer_cep = ''.join(cep for cep in self.customer["CEP"] if cep.isdigit())
                email = None
                customer_pj = True

                try:
                    customer_email = validate_email(self.customer["Email"], check_deliverability=False)
                    email = customer_email.normalized
                except EmailNotValidError as error:
                    self.logger.warning(f'Customer email {self.customer["Email"]} is invalid')
                    customer_messages["warning"] = f'Customer email {self.customer["Email"]} is invalid'

                if len(customer_idenfity) == 11:
                    customer_pj = False

                cnpj = self.customer["CNPJ"] if customer_pj == True else None
                cpf = self.customer["CNPJ"] if customer_pj == False else None
                razao_social = self.customer["Razão Social"]
                telefone = self.customer["Telefone"] if len(customer_phone) == 10 or len(customer_phone) == 11 else None
                nome_fantasia = self.customer["Nome Fantasia"]

                try:
                    customer_data["customer"] = CustomerData(email=email, razao_social=razao_social, nome_fantasia=nome_fantasia, telefone=telefone, cpf=cpf, cnpj=cnpj)
                    customer_data["address"] = None
                except Exception as error:
                    customer_messages["error"] = f'Customer data error {self.customer["CNPJ"]}'
                    self.logger.error(f'Error during try get customer data {str(error)}')

                if len(customer_cep) == 8:
                    address_search = await self.call_external_cep_api(self.customer["CEP"])
                    if address_search:
                        customer_data["address"] = address_search
            else:
                customer_messages["error"] = 'Customer identify "CPF/CNPJ" or "Razão Social" is invalid'
                self.logger.error(f'Customer identify is invalid {self.customer}')
        else:
            customer_messages["error"] = f'Invalid customer data'
            self.logger.error(f'Invalid customer data {self.customer}')

        return customer_data, customer_messages
    
    async def call_external_cep_api(self, zip_code):
        address_data = None
        if zip_code != None:
            async with httpx.AsyncClient() as client:
                address = await client.get(f'https://viacep.com.br/ws/{zip_code}/json/')
                address_data = address.json()

        return address_data
