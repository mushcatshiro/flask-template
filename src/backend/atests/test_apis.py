from backend.app import create_app
import unittest


class FlaskApiAPITest(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        # db.create_all()
        self.client = self.app.test_client()

    def tearDown(self):
        # db.session.remove()
        # db.drop_all()
        self.app_context.pop()

    def test_api_hello_world(self):
        response = self.client.get('/api/v1/')
        rv = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(rv, {"response": "hello world"})

    def test_api_read_todos(self):
        response = self.client.get('/api/v1/read/todos')
        print(response.data)
        self.assertEqual(response.status_code, 200)

    def _test_api_read_todo_by_id(self):
        response = self.client.get('/api/v1/read/todo/1')
        print(response.data)
        self.assertEqual(response.status_code, 200)
        print(response.json())
