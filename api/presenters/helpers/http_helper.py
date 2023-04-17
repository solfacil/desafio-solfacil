from typing import Any, TypedDict


class HttpResponse(TypedDict):
    """Class to http_response representation"""

    status_code: int
    body: Any


class ServerError(Exception):
    def __init__(self):
        super().__init__("Internal server error")


def bad_request(error: Exception) -> HttpResponse:
    return {"status_code": 400, "body": error}


def server_error() -> HttpResponse:
    return {"status_code": 500, "body": ServerError()}


def created() -> HttpResponse:
    return {"status_code": 201, "body": None}


def ok(data: Any) -> HttpResponse:
    return {"status_code": 200, "body": data}
