from backend.app import create_app, db
import unittest
import json


class FlaskApiAPITest(unittest.TestCase):
    """docstring for FlaskAPITest"""

    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_api_hellow_world(self):
        response = self.client.get('/api/v1/')
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json_response, {"response": "hello world"})


"""
test cases
- [] create
- [] delete non exist, also check error here
- [] read
- [] update
- [] read update
- [] delete
- [] ensure db empty
"""
