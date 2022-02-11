import logging
import os
import unittest


from backend.app.business_logic.connection_utils import SqlAConnectionSession
from backend.app.business_logic import SqlAConnectionError
from backend.app.business_logic.models import Todo


logger = logging.getLogger(__name__)


class SqlAConnectionTest(unittest.TestCase):
    def setUp(self):
        self.conn_uri = os.environ.get('SQLALCHEMYDBURI')
        self.wrong_conn_uri = os.environ.get('SQLALCHEMYDBWRONGURI')
        with SqlAConnectionSession(
            self.conn_uri
        ) as db:
            db.conn.execute(
                'CREATE TABLE IF NOT EXISTS test_todos ('
                'id serial PRIMARY KEY, '
                'name VARCHAR(64), '
                'descr VARCHAR(64));'
            )
            db.conn.commit()

    def tearDown(self):
        with SqlAConnectionSession(
            self.conn_uri,
        ) as db:
            db.conn.execute(
                'DROP TABLE test_todos'
            )
            db.conn.commit()

    def _test_query(self):
        with SqlAConnectionSession(
            self.conn_uri,
        ) as db:
            result = db.conn.query(Todo).all()
            logger.info(f'queried result: {result}')
        self.assertTrue(result)

    def _test_create(self):
        todo = {
            'name': 'new todo',
            'descr': 'new todo for testing'
        }

        with SqlAConnectionSession(
            self.conn_uri
        ) as db:
            db_todo = Todo(**todo)
            db.conn.add(db_todo)
            db.conn.commit()
            db.conn.refresh(db_todo)
            logger.info(f'new added record: {db_todo}')

    def test_run(self):
        self._test_create()
        self._test_query()

    def test_failed_conn(self):
        with self.assertRaises(SqlAConnectionError):
            SqlAConnectionSession(
                self.wrong_conn_uri
            )
