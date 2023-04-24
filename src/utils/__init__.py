# from typing import Optional

# from pydantic import BaseModel, Field


# class PartnerSchema(BaseModel):
#     partner_id: str = Field(alias="id_parceiro")
#     cnpj: str
#     company_name: Optional[str] = Field(alias="razao_social")
#     trade_name: Optional[str] = Field(alias="nome_fantasia")
#     phone: Optional[str] = Field(alias="telefone")
#     email: Optional[str]
#     zip_code: str = Field(alias="cep")


# obj_en = {
#     "partner_id": "8b809400-9614-4fa0-a45c-a34ef4c429a0",
#     "cnpj": "69971725000123",
#     "company_name": None,
#     "trade_name": None,
#     "phone": None,
#     "email": "company@company.com",
#     "zip_code": "01156325",
# }

# print(PartnerSchema(**obj_en))
