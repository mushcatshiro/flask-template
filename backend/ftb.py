import os
from flask_migrate import Migrate
from backend.app import create_app, db
from backend.app.models import Todo
import click


app = create_app(os.getenv('FLASK_CONFIG') or 'testing')
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Todo=Todo)  # to include models


@app.cli.command()
@click.option('--message', required=True)
def setup(message):
    """initial database setup"""

    import flask_migrate
    flask_migrate.init()
    flask_migrate.migrate(message=message)
    flask_migrate.upgrade()


@app.cli.command()
def deploy():
    """Run deployment tasks."""

    import flask_migrate
    flask_migrate.migrate(message="init")
    flask_migrate.upgrade()
