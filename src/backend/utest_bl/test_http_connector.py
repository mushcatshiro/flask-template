import unittest
import urllib3


from backend.app.business_logic.connection_utils import HttpConnectionSession  # noqa
# from backend.app.business_logic import HttpConnectionError


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class HttpConnectionTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_request_success(self):
        with HttpConnectionSession() as conn:
            resp = conn.get('https://google.com', verify=False)
        self.assertIn('google', resp.text)
        self.assertEqual(resp.status_code, 200)

    def test_get_request_fail(self):
        with self.assertRaises(Exception):
            with HttpConnectionSession() as conn:
                conn.get('https://google.com123')
