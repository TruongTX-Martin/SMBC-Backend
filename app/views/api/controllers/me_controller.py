from flask import Blueprint, redirect, request
from flask import Blueprint, current_app, g, request
from injector import inject

from ....exceptions import LogicError, NotFoundError, ParameterError
from ....middlewares.authenticate import token_required
from app.middlewares.request_log import request_log
from ..responses import Error, User

app = Blueprint('api.me', __name__)


@app.route('', methods=["GET"])
@request_log
@inject
@token_required
def me():
    user = g.user
    return User(model=user).response(), 200

