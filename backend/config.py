import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    PROJECT_NAME = 'RANDOM_PROJECT_NAME'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'R4nd0MS3cret'
    MAIL_SERVER = None  # pending setup
    MAIL_PORT = None  # pending setup
    MAIL_USERNAME = None  # pending setup
    MAIL_PASSWORD = None  # pending setup
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = False
    BASEDIR = basedir

    # redis :// [[username :] password@] host [: port] [/ database]
    CELERY_BROKER_URL = os.getenv("REDIS_URI")

    # postgresql://[user[:password]@][netloc][:port][,...][/dbname]
    SQLALCHEMY_DATABASE_URI = os.getenv("PG_DATABASE_URI")

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    """
    spec:
    env - windows
    """
    DEBUG = True


class TestingConfig(Config):
    """
    spec:
    env - windows
    """
    TESTING = True

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

        import logging
        from flask.logging import default_handler

        # to come back and look at logging
        app.logger.removeHandler(default_handler)

        logfile_handler = logging.FileHandler(
            os.path.join(cls.BASEDIR, f'{cls.PROJECT_NAME}-TEST.log')

        )
        app.logger.addHandler(logfile_handler)


class ProductionConfig(Config):
    """
    spec:
    env - windows
    """
    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

        import logging
        from flask.logging import default_handler

        # to come back and look at logging
        app.logger.removeHandler(default_handler)

        logfile_handler = logging.FileHandler(
            os.path.join(cls.BASEDIR, f'{cls.PROJECT_NAME}-PROD.log')

        )
        app.logger.addHandler(logfile_handler)


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
