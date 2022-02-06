import os
from backend.app import create_app
import click


app = create_app(os.getenv('FLASK_CONFIG') or 'testing')


@app.cli.command()
@click.option('--message', required=True)
def atest(message):
    pass
