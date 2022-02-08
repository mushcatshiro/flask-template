from backend.app import celery
import time


@celery.task
def sample_task():
    time.sleep(5)
    print('hi')
