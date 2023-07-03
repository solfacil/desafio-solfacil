from json import dumps

from fastapi import Response

from src.domain.enums.http_response.internal_code import InternalCode


class ResponseModel:
    def __init__(
        self,
        success: bool,
        internal_code: InternalCode,
        message: str = None,
        result: any = None,
    ):
        self.internal_code = internal_code
        self.message = message
        self.result = result
        self.success = success
        self.response = self.to_dumps()

    def to_dumps(self) -> str:
        response_model = dumps(
            {
                "result": self.result,
                "message": self.message,
                "success": self.success,
                "internal_code": self.internal_code,
            }
        )
        return response_model

    def build_http_response(
        self,
        status_code: int,
    ) -> Response:
        http_response = Response(
            content=self.response,
            status_code=status_code,
            headers={"Content-type": "application/json"},
        )
        return http_response
