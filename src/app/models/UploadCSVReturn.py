from models.Partner import Partner
from pydantic import BaseModel


class UploadCSVReturn(BaseModel):
    loaded: list[Partner]
    errors: list[dict]

    class Config:
        arbitrary_types_allowed = True
