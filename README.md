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
  - [x] contextmanager base class
  - [x] http conn
  - [x] db conn
  - [x] sqlalchemy conn
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
  - [ ] sqlalchemy
- [ ] logging for unit testing
- [ ] exceptions logging and user message

### contentious issues

the test for celery tasks are not testing celery's behavior. celery testing will be available later once the author have found a much elagant way of doing things or is convinved by the methods presented.
