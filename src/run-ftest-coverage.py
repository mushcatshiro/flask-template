import coverage
import os
import unittest


def coverage_decorator(func):
    def _coverage_decorator(*args, **kwargs):
        COV = coverage.coverage(branch=True, include='backend/app/api/*')
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
    tests = unittest.TestLoader().discover('backend/ftests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    run()
