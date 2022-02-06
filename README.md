# flask-template

flask quick start template. to add cookiecutter. assuming development in unix environment


## getting started

``` bash
>> cd backend
>> set flask_app=ftb.py
>> flask setup --message "initialize database for first time"
# or flask deploy if database has been initialized
>> flask run

# in separate terminal
>> celery -A backend.celery_worker.celery worker -l INFO
```

## backlog

- [x] removing flask track usage
- [ ] business logic
  - [ ] http conn
  - [ ] db conn
  - [ ] unit testing
  - [x] hook setup
  - [x] exception base class
  - [ ] mixin(s)
- [ ] flask app testing
- [ ] post deployment testing script
- [x] support multiple requirements.txt
- [ ] adding dockerfile and docker-compose
- [ ] production support
- [ ] thread job support
- [ ] more celery support
- [ ] cookiecutter support
  - [ ] CORS
  - [ ] celery
