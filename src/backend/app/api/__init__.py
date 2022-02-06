from flask import Blueprint

api = Blueprint('api', __name__)


from .v1 import api_v1
# from .v2 import api_v2
from . import hook

api.register_blueprint(api_v1)
# api.register_blueprint(api_v2)
