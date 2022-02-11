from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .connection_base import ConnectionBaseClass
from ..custom_exceptions import SqlAConnectionError


class SqlAConnectionSession(ConnectionBaseClass):
    def __init__(self, conn_uri):
        try:
            engine = create_engine(
                conn_uri,
                pool_pre_ping=True
            )
            sessionlocal = sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=engine
            )
            conn = sessionlocal()
            super().__init__(conn=conn)
        except Exception:
            raise SqlAConnectionError(
                'database connection error',
                'failed to connect with URI provided'
            )
