class BaseException(Exception):
    def __init__(self, message, err_message, status_code=None):
        super(Exception, self).__init__()
        self.err_message = err_message
        self.message = message
        if status_code is None:
            self.status_code = 400


class HttpConnectionError(BaseException):
    pass


class PsqlConnectionError(BaseException):
    pass


class SqlAConnectionError(BaseException):
    pass
