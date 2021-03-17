import os
from backend.app import celery, create_app  # noqa

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
app.app_context().push()
