import requests as r


from .connection_base import ConnectionBaseClass


class HttpConnectionSession(ConnectionBaseClass):
    def __init__(self):
        super().__init__(r.Session())
        self.conn.trust_env = False

    def __enter__(self):
        return self.conn
