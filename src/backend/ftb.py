import os
from backend.app import create_app
import click


app = create_app(os.environ.get('FLASKCONFIG') or 'testing')


@app.cli.command()
@click.option('--message', required=True)
def atest(message):
    pass
