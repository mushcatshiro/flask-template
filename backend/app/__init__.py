from flask import Flask, jsonify
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_track_usage import TrackUsage
from backend.config import config, Config
from celery import Celery


db = SQLAlchemy()
ma = Marshmallow()
celery = Celery(
    __name__,
    broker=Config.CELERY_BROKER_URL,
    # backend='db+sqlite:///results.sqlite'
)
track = TrackUsage()


def create_app(config_name):
    app = Flask(__name__)
    print(config_name)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    ma.init_app(app)
    celery.conf.update(app.config)

    from flask_track_usage.storage.sql import SQLStorage
    with app.app_context():
        track.init_app(app, [SQLStorage(db=db)])

    from backend.app.api.sample_api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')


    register_error(app)

    return app


def register_error(app):
    @app.errorhandler(400)
    def bad_request(e):
        print(e)
        # jsonify({"msg": "bad request"})
        return "bad request", 400

    @app.errorhandler(404)
    def page_not_found(e):
        return jsonify({"msg": "page not found"}), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return jsonify({"msg": "internal server error"}), 500
