from src.domain.validators.partners.validator import PartnersValidator

from base64 import b64decode


class PartnersService:

    @staticmethod
    async def load_from_csv(payload: PartnersValidator):



