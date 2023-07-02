from base64 import b64decode

from src.domain.exceptions.service.exception import Base64DecodeError
from src.domain.validators.partners.validator import PartnersValidator


class CsvService:

    @staticmethod
    async def decode_b64_to_csv(payload: PartnersValidator):
        try:
            partners_csv = b64decode(payload)
            return partners_csv

        except Exception as ex:
            raise Base64DecodeError()


    @staticmethod
    async def get_partners_model_from_csv(csv):
        pass