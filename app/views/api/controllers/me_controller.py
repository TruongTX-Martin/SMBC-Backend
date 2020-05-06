from flask import Blueprint, redirect, request
from flask_login import current_user
from injector import inject

from ....exceptions import LogicError, NotFoundError, ParameterError
from ....middlewares.login_as_anonymous import login_as_anonymous
from ..responses import Error, User

app = Blueprint('api.me', __name__)


@app.route('', methods=["GET"])
@inject
@login_as_anonymous
def me():
    user = current_user
    return User(model=user).response(), 200
