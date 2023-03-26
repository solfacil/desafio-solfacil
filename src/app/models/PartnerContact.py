import re

from pydantic import BaseModel, validator


class PartnerContact(BaseModel):
    telefone: str
    email: str

    class Config:
        orm_mode = True

    @validator('telefone', pre=True)
    def validate_telefone(cls, v: str):
        only_numbers = re.sub(r'[^\d]', '', v)
        # may apply mask based on digits number lik 11 = ddd+cellphone, but if no DDD, then mask would break 🤔
        return only_numbers

    @validator('email', pre=True)
    def validate_email(cls, v: str):
        v = v.encode('utf-8')
        return v
