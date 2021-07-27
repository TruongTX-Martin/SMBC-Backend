from functools import wraps
import time

from flask import current_app, g, request


def request_log(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        start_time = time.time()

        try:
            response = f(*args, **kwargs)

            duration = round(time.time() - start_time, 2)
            current_app.logger.info(
                f"%s %s path=%s response_status=%s user_agent=%s user_id=%s duration=%s",
                request.remote_addr, request.method, request.path, 'success',
                request.user_agent, g.user.id if
                ('user' in g and g.user is not None) else 'anonymous',
                duration)

            return response
        except Exception as e:
            duration = round(time.time() - start_time, 2)
            current_app.logger.info(
                f"%s %s path=%s response_status=%s user_agent=%s user_id=%s duration=%s",
                request.remote_addr, request.method, request.path, 'error',
                request.user_agent, g.user.id if
                ('user' in g and g.user is not None) else 'anonymous',
                duration)

            raise e

    return decorated
