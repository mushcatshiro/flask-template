import datetime as dt


from flask import current_app, g, jsonify, request, _request_ctx_stack
from marshmallow import ValidationError


from . import api
from backend.app.business_logic.custom_exceptions import BaseException


@api.before_request
def set_g_variable():
    g.request_in_time = dt.datetime.now()
    if request.method == 'POST':
        g.context = request.json
    elif request.method == 'GET':
        g.context = ''
    else:
        raise NotImplementedError


@api.after_request
def log_request(response):
    ctx = _request_ctx_stack.top
    request_duration = (dt.datetime.now() - g.request_in_time)\
        .total_seconds()
    data = {
        'url': ctx.request.url,
        'method': ctx.request.method,
        'app_name': ctx.app.name,
        'blueprint': ctx.request.blueprint,
        'view_args': ctx.request.view_args,
        'status_code': response.status_code,
        'speed': float(request_duration),
        'payload': g.context,
    }
    current_app.logger.info(f'after request logging: {data}')
    return response


@api.errorhandler(BaseException)
def error_response(e):
    current_app.logger(e)
    return jsonify(
        {
            'error': e.__class__.__name__,
            'message': e.message
        }
    ), e.status_code


@api.errorhandler(ValidationError)
def schema_validation_error(e):
    current_app.logger(e)
    return jsonify(
        {
            'error': e.__class__.__name__,
            'message': e.message
        }
    ), 400
