from flask import Flask, jsonify
from flask_marshmallow import Marshmallow
from backend.config import config, CeleryConfig
# from celery import Celery
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
ma = Marshmallow()
'''
celery = Celery(
    __name__,
    broker=CeleryConfig.CELERY_BROKER_URL,
    backend=CeleryConfig.CELERY_BROKER_URL
)
'''


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    ma.init_app(app)
    # celery.conf.update(app.config)
    # update_celery(app, celery)


    from backend.app.api import api as api_blueprint
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

'''
def update_celery(app, celery):
    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)
    celery.Task = ContextTask
    return celery
'''
