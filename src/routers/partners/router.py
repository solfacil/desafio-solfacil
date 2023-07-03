from http import HTTPStatus
from typing import List

from fastapi import APIRouter, Response, UploadFile

from src.domain.enums.http_response.internal_code import InternalCode
from src.domain.models.http_response.model import ResponseModel
from src.domain.validators.request.csv.validator import CsvValidator
from src.domain.validators.response.partners.validator import PartnersResponse
from src.services.partners.service import PartnersService


class PartnersRouter:
    __router = APIRouter(prefix="/api/v1", tags=["Partners Loader"])

    @staticmethod
    def get_partners_router():
        return PartnersRouter.__router

    @staticmethod
    @__router.post("/partners/uploadfile")
    async def create_upload_file(file: UploadFile) -> Response:
        CsvValidator(file=file)
        message = await PartnersService.load_from_csv_file(file=file)
        response = ResponseModel(
            message=message, internal_code=InternalCode.SUCCESS, success=True
        ).build_http_response(
            status_code=HTTPStatus.OK,
        )
        return response

    @staticmethod
    @__router.get("/partners", response_model=List[PartnersResponse])
    async def create_upload_file() -> Response:
        result = await PartnersService.get_all_partners()
        response = ResponseModel(
            result=result, internal_code=InternalCode.SUCCESS, success=True
        ).build_http_response(
            status_code=HTTPStatus.OK,
        )
        return response
