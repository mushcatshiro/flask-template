import os

import click
from flask_migrate import Migrate, upgrade, init, migrate

from backend.app import create_app, db
from backend.app.business_logic.models import (
    Project_Name, Project_Status
)


app = create_app(os.environ.get('FLASKCONFIG') or 'testing')
migrate_instance = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(
        db=db,
        Project_Name=Project_Name,
        Project_Status=Project_Status
    )


@app.cli.command()
def initialize():
    init()
    migrate()


@app.cli.command()
@click.option('--execute', default=False)
def deploy(execute):
    migrate()
    if execute:
        upgrade()
