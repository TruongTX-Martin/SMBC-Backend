from functools import wraps

from flask import request


def validate_request_body(schema):
    def execute(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            schema().load(request.get_json())
            return f(*args, **kwargs)

        return decorated

    return execute
