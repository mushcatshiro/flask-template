from flask import Blueprint

api = Blueprint('sample_todo_api', __name__)

from . import todo
