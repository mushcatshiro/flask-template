from threading import Thread


from flask import jsonify


from backend.app.api.v2 import api_v2
from backend.app.tasks.threaded_task import tasync_sample_job


@api_v2.route('/')
def run_tasync_job():
    Thread(target=tasync_sample_job).start()
    return jsonify({"response": 'hello world'})
