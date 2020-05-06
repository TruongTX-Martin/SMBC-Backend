from functools import wraps

from flask import Flask, jsonify, make_response, request
from injector import inject
import jwt

from app.config import Config
from app.exceptions.parameter_error import ParameterError
from app.services import UserService


@inject
def token_required(func):
    @wraps(func)
    @inject
    def decorator(user_service: UserService, *args, **kwargs):
        header = request.headers.get('Authorization')
        try:
            _, token = header.split()
            decoded = jwt.decode(token, Config.SECRET_KEY, algorithms='HS256')
            user_service.load_logged_in_user_to_request(decoded['id'])
        except AttributeError as e:
            raise ParameterError('Token does not exist. {}'.format(e),
                                 status_code=401)
        except jwt.DecodeError as e:
            raise ParameterError('Token is not valid. {}'.format(e),
                                 status_code=401)
        except jwt.ExpiredSignatureError as e:
            raise ParameterError('Token is expired. {}'.format(e),
                                 status_code=401)
        return func(*args, **kwargs)

    return decorator
