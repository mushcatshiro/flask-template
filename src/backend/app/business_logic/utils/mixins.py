from ..connection_utils import HttpConnectionSession


class HttpConnectionMixin:

    def get_request(self, config):
        with HttpConnectionSession() as conn:
            resp = conn.get(
                config['url']
            )
        return resp.json()

    def post_request(self, config):
        with HttpConnectionSession() as conn:
            resp = conn.post(
                config['url'],
                config['payload']
            )
        return resp.json()
