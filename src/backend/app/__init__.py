from flask import Flask, jsonify
from flask_marshmallow import Marshmallow
from backend.config import config
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
ma = Marshmallow()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    ma.init_app(app)


    from backend.app.api import api as api_blueprint
    from backend.app.api.v1 import api_v1
    api_blueprint.register_blueprint(api_v1, url_prefix='/v1')
    app.register_blueprint(api_blueprint, url_prefix='/api')


    register_error(app)

    return app


def register_error(app):
    @app.errorhandler(400)
    def bad_request(e):
        return jsonify({"msg": "bad request"}), 400

    @app.errorhandler(404)
    def page_not_found(e):
        return jsonify({"msg": "page not found"}), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return jsonify({"msg": "internal server error"}), 500