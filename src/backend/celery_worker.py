import logging
import os

from backend.app import celery, create_app  # noqa

from celery.signals import after_setup_task_logger, after_setup_logger


basedir = os.path.abspath(os.path.dirname(__name__))


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
app.app_context().push()


def setup_file_handler_logger(logger, formatter):
    logfile_handler = logging.FileHandler(
        os.path.join(basedir, 'celery-instance.log')
    )
    logfile_handler.setFormatter(formatter)
    logfile_handler.setLevel(logging.INFO)
    logger.addHandler(logfile_handler)


# for celery global logger
@after_setup_logger.connect
def setup_celery_global_logger(logger, *args, **kwargs):
    formatter = logging.Formatter(
        '[%(asctime)s: %(levelname)s in %(module)s] %(message)s'
    )
    setup_file_handler_logger(logger, formatter)


@after_setup_task_logger.connect
def setup_celery_task_logger(logger, *args, **kwargs):
    formatter = logging.Formatter(
        '[%(asctime)s: %(levelname)s in %(module)s] %(message)s'
    )
    setup_file_handler_logger(logger, formatter)
