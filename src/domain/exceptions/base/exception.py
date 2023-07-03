from src.domain.enums.http_response.internal_code import InternalCode


class DomainException(Exception):
    def __init__(
        self,
        msg: str,
        status_code: int,
        internal_code: InternalCode,
        success: bool,
        *args,
        **kwargs
    ):
        self.internal_code = internal_code
        self.success = success
        self.msg = msg
        self.status_code = status_code
        super().__init__(*args, **kwargs)


class RepositoryException(Exception):
    def __init__(
        self,
        msg: str,
        status_code: int,
        internal_code: InternalCode,
        success: bool,
        *args,
        **kwargs
    ):
        self.internal_code = internal_code
        self.success = success
        self.msg = msg
        self.status_code = status_code
        super().__init__(*args, **kwargs)


class ServiceException(Exception):
    def __init__(
        self,
        msg: str,
        status_code: int,
        internal_code: InternalCode,
        success: bool,
        *args,
        **kwargs
    ):
        self.internal_code = internal_code
        self.success = success
        self.msg = msg
        self.status_code = status_code
        super().__init__(*args, **kwargs)
