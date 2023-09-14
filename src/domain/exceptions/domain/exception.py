from http import HTTPStatus

from src.domain.enums.http_response.internal_code import InternalCode
from src.domain.exceptions.base.exception import DomainException


class InvalidFileTypeError(DomainException):
    def __init__(self, *args, **kwargs):
        self.msg = 'File type must be ".csv"'
        self.status_code = HTTPStatus.BAD_REQUEST
        self.internal_code = InternalCode.DATA_VALIDATION_ERROR
        self.success = False
        super().__init__(
            self.msg,
            self.status_code,
            self.internal_code,
            self.success,
            *args,
            **kwargs
        )
