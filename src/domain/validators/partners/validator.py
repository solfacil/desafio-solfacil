import base64

from pydantic import BaseModel

class PartnersValidator(BaseModel):
    csv_data: base64