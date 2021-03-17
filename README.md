# flask-template

flask quick start template. to add cookiecutter.


## getting started

``` bash
>> cd backend
>> set flask_app=ftb.py
>> flask setup --message "initialize database for first time"
# or flask deploy if database has been initialized
>> flask run

# in separate terminal
>> celery -A backend.celery_worker.celery worker
```