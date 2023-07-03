from http import HTTPStatus
from time import time

import loglifos
from fastapi import Request, Response

from src.domain.enums.http_response.internal_code import InternalCode
from src.domain.exceptions.domain.exception import DomainException
from src.domain.exceptions.service.exception import ServiceException
from src.domain.models.http_response.model import ResponseModel
from src.routers.base.app import AmaterasuApp


class Middleware:
    app = AmaterasuApp.get_app()

    @classmethod
    @app.middleware("http")
    async def process_request(cls, request: Request, call_next: callable) -> Response:
        start_time = time()
        response = await cls.__response_handler(request=request, call_next=call_next)
        process_time = time() - start_time
        response.headers["X-Process-Time"] = str(process_time)
        return response

    @staticmethod
    async def __response_handler(request: Request, call_next: callable):
        response = None

        try:
            response = await call_next(request)

        except DomainException as ex:
            loglifos.info(msg=ex.msg)
            response = ResponseModel(
                success=False, message=ex.msg, internal_code=ex.internal_code
            ).build_http_response(status_code=ex.status_code)

        except ServiceException as ex:
            loglifos.info(msg=ex.msg)
            response = ResponseModel(
                success=False, message=ex.msg, internal_code=ex.internal_code
            ).build_http_response(status_code=ex.status_code)

        except Exception as ex:
            loglifos.error(exception=ex, msg=str(ex))
            response = ResponseModel(
                success=False, internal_code=InternalCode.INTERNAL_SERVER_ERROR
            ).build_http_response(status_code=HTTPStatus.INTERNAL_SERVER_ERROR)

        finally:
            return response
