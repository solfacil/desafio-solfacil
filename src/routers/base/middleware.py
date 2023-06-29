from http import HTTPStatus
from time import time

import loglifos
from fastapi import Request, Response

from src.domain.enums.http_response.internal_code import InternalCode
from src.domain.models.http_response.model import ResponseModel
from src.routers.base.app import AmaterasuApp


class Middleware:

    app = AmaterasuApp.get_app()

    @classmethod
    @app.middleware("http")
    async def process_request(cls, request: Request, call_next: callable) -> Response:
        start_time = time()
        response = await cls.response_handler(request=request, call_next=call_next)
        process_time = time() - start_time
        response.headers["X-Process-Time"] = str(process_time)

        return response

    @staticmethod
    async def response_handler(request: Request, call_next: callable):
        response = None

        try:
            response = await call_next(request)

        except Exception as ex:
            loglifos.error(exception=ex, msg=str(ex))

            response = ResponseModel(
                success=False, internal_code=InternalCode.INTERNAL_SERVER_ERROR
            ).build_http_response(status_code=HTTPStatus.INTERNAL_SERVER_ERROR)

        finally:

            return response
