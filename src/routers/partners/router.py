from fastapi import APIRouter, Response

from src.domain.enums.http_response.internal_code import InternalCode
from src.domain.models.http_response.model import ResponseModel
from src.domain.validators.partners.validator import PartnersValidator

from http import HTTPStatus

class PartnersRouter:

    __router = APIRouter(prefix="/api/v1", tags=["Partners Loader"])


    @classmethod
    def get_partners_router(cls):
        return  cls.__router

    @staticmethod
    @__router.put("/partners", response_model="xxx")
    async def load_partners(payload: PartnersValidator) -> Response:
        message = await PartnersService.load_from_csv(payload=payload)
        # message = "Partners uploaded successfully."
        response = ResponseModel(
            message=message, internal_code=InternalCode.SUCCESS, success=True
        ).build_http_response(status_code=HTTPStatus.OK, )
        return response

