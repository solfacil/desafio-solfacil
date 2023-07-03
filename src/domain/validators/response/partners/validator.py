from pydantic import BaseModel


class PartnersResponse(BaseModel):
    cnpj: str
    company_name: str
    fantasy_name: str
    phone: str
    email: str
    zipcode: str
