import psycopg2 as p
import psycopg2.extras as pex


from .connection_base import ConnectionBaseClass
from ..custom_exceptions import PsqlConnectionError


class PostgresConnectionSession(ConnectionBaseClass):
    def __init__(
        self,
        host,
        username,
        password,
        port
    ):
        try:
            conn = p.connect(
                host=host,
                user=username,
                password=password,
                port=port
            )
            super().__init__(conn=conn)
            self.cursor = self.conn.cursor(
                cursor_factory=pex.DictCursor
            )
        except Exception:
            raise PsqlConnectionError(
                'database connection error',
                'failed to create connection '
                f'to {host}:{port} '
                f'with user: {username}'
            )
