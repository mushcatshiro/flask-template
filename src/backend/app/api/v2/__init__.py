from flask import Blueprint

api_v2 = Blueprint('api_v2', __name__, url_prefix='/v22')

from . import endpoint
