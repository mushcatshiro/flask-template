class BaseException(Exception):
    def __init__(self, message, err_message, status_code=None):
        self.err_message = err_message
        self.message = message
        if status_code is None:
            status_code = 400
        self.status_code = status_code
        # super().__init__(self.err_message)


class HttpConnectionError(BaseException):
    def __init__(self, message, err_message, status_code=None):
        super().__init__(
            message=message,
            err_message=err_message,
            status_code=status_code
        )


class PsqlConnectionError(BaseException):
    pass


class SqlAConnectionError(BaseException):
    pass


class ResourceNotFoundError(BaseException):
    def __init__(self, message, err_message, status_code):
        super().__init__(
            message,
            err_message,
            status_code
        )
