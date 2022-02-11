import os
import unittest


from backend.app.business_logic.connection_utils import PostgresConnectionSession  # noqa
from backend.app.business_logic import PsqlConnectionError


class PsqlConnectionTest(unittest.TestCase):
    def setUp(self):
        self.host = os.environ.get('PGHOST')
        self.user = os.environ.get('PGUSER')
        self.pasw = os.environ.get('PGPASW')
        self.port = os.environ.get('PGPORT')
        self.wpsw = os.environ.get('PGWPSW')
        with PostgresConnectionSession(
            self.host,
            self.user,
            self.pasw,
            self.port
        ) as db:
            db.cursor.execute(
                'CREATE TABLE IF NOT EXISTS test_todos ('
                'id serial PRIMARY KEY, '
                'name VARCHAR(64), '
                'descr VARCHAR(64));'
            )
            db.conn.commit()

    def tearDown(self):
        with PostgresConnectionSession(
            self.host,
            self.user,
            self.pasw,
            self.port
        ) as db:
            db.cursor.execute(
                'DROP TABLE test_todos'
            )
            db.conn.commit()

    def _test_query(self):
        with PostgresConnectionSession(
            self.host,
            self.user,
            self.pasw,
            self.port
        ) as db:
            db.cursor.execute('SELECT * FROM test_todos;')
            result = db.cursor.fetchall()
        self.assertTrue(result)

    def _test_create(self):
        with PostgresConnectionSession(
            self.host,
            self.user,
            self.pasw,
            self.port
        ) as db:
            db.cursor.execute(
                "INSERT INTO test_todos (name, descr) "
                "VALUES ('todo1', 'test1');"
            )
            db.conn.commit()

    def test_run(self):
        self._test_create()
        self._test_query()

    def test_failed_conn(self):
        with self.assertRaises(PsqlConnectionError):
            PostgresConnectionSession(
                self.host,
                self.user,
                self.wpsw,
                self.port
            )
