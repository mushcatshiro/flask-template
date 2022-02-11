import logging
import os
import unittest


import coverage
from dotenv import load_dotenv


load_dotenv('.env.utest_bl')


def coverage_decorator(func):
    def _coverage_decorator(*args, **kwargs):
        COV = coverage.coverage(branch=True, include='backend/app/business_logic/*')  # noqa
        COV.start()
        func(*args, **kwargs)
        COV.stop()
        COV.save()
        print('Coverage Summary:')
        COV.report()
        basedir = os.path.abspath(os.path.dirname(__file__))
        covdir = os.path.join(basedir, 'tmp/coverage')
        COV.html_report(directory=covdir)
        print('HTML version: file://%s/index.html' % covdir)
        COV.erase()
        return
    return _coverage_decorator


@coverage_decorator
def run():
    tests = unittest.TestLoader().discover('backend/utest_bl')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    PROJECT_NAME = os.environ.get('PROJECT_NAME')
    formatter = logging.Formatter(
        '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
    )
    logfile_handler = logging.FileHandler(
        os.path.join(
            f'{PROJECT_NAME}-UTEST-BL.log'
        )

    )
    logfile_handler.setFormatter(formatter)
    logfile_handler.setLevel(logging.DEBUG)
    logger.addHandler(logfile_handler)
    run()
