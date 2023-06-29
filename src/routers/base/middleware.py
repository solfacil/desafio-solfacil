from time import time
from http import HTTPStatus

from fastapi import Request, Response
import loglifos

from src.domain.enums.http_response.internal_code import InternalCode
from src.domain.models.http_response.model import ResponseModel
from src.routers.base.app import AmaterasuApp


class RequestMiddleware:

    app = AmaterasuApp.get_app()

    @staticmethod
    @app.middleware("http")
    async def process_request(request: Request, call_next) -> Response:
        start_time = time()
        response = await call_next(request)
        process_time = time() - start_time
        response.headers["X-Process-Time"] = str(process_time)
        return response

    @staticmethod
    async def exception_control(request: Request, call_next: callable):
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
