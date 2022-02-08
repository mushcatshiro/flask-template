from abc import ABC, abstractmethod
import logging


logger = logging.getLogger(__name__)


class ConnectionBaseClass(ABC):
    @abstractmethod
    def __init__(self, conn):
        self.conn = conn

    def __enter__(self):
        return self

    def __exit__(self, exec_type, exec_value, exec_traceback):
        self.conn.close()
        if exec_type or exec_value:
            logger.error(exec_type)
            return False
        return True
