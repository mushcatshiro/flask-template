import logging
import os


from flask import request
from dotenv import load_dotenv


load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__))


class RequestFormatter(logging.Formatter):
    def format(self, record):
        record.request_ip = request.remote_addr
        return super().format(record)


class CeleryConfig:
    # redis :// [[username :] password@] host [: port] [/ database]
    broker_url = os.environ.get('CELERY_BROKER_URL')
    backend_result_storage = os.environ.get('CELERY_BACKEND_RESULT_STORAGE')


class Config:
    PROJECT_NAME = os.environ.get('PROJECT_NAME')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'R4nd0MS3cret'
    MAIL_SERVER = None  # pending setup
    MAIL_PORT = None  # pending setup
    MAIL_USERNAME = None  # pending setup
    MAIL_PASSWORD = None  # pending setup
    '''
    hint:
    psql        - postgresql+psycopg2://user:pass@host:port/dbname
    mssql       - mysql+pymysql://user:password@host:port/dbname
    sqlite/win  - sqlite:///C:\\path\\to\\foo.db
    sqlite/unix - sqlite:////absolute/path/to/foo.db
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMYDBURI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BASEDIR = basedir
    PSQLDB = {
        'host': os.environ.get('PSQLDBHOST'),
        'username': os.environ.get('PSQLDBUSERNAME'),
        'password': os.environ.get('PSQLDBPASSWORD'),
        'port': os.environ.get('PSQLDBPORT'),
        'dbtype': 'psql',
        'as_dict': True
    }

    @staticmethod
    def init_app(app):
        pass


class TestingConfig(Config):

    TESTING = True

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

        import logging
        from flask.logging import default_handler

        app.logger.removeHandler(default_handler)
        app.logger.setLevel(logging.DEBUG)
        formatter = RequestFormatter(
            '[%(asctime)s] '
            '%(levelname)s in %(module)s: %(message)s'
        )

        logfile_handler = logging.FileHandler(
            os.path.join(cls.BASEDIR, f'{cls.PROJECT_NAME}-TEST.log')

        )
        logfile_handler.setFormatter(formatter)
        logfile_handler.setLevel(logging.DEBUG)
        app.logger.addHandler(logfile_handler)


class ProductionConfig(Config):

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

        import logging
        from flask.logging import default_handler

        app.logger.removeHandler(default_handler)
        app.logger.setLevel(logging.INFO)
        formatter = RequestFormatter(
            '[%(asctime)s] %(request_ip)s payload: %(context)s ',
            '%(levelname)s in %(module)s: %(message)s'
        )

        logfile_handler = logging.RotatingFileHandler(
            os.path.join(cls.BASEDIR, f'{cls.PROJECT_NAME}-PROD.log'),
            maxBytes=102400,
            backupCount=10,
            encoding='UTF-8'

        )
        logfile_handler.setFormatter(formatter)
        logfile_handler.setLevel(logging.INFO)
        app.logger.addHandler(logfile_handler)


class DockerConfig(Config):

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


config = {
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': TestingConfig
}
