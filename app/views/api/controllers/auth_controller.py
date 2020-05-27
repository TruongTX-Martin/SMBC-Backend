from flask import Blueprint, current_app, g, request
from injector import inject

from app.services import UserService
from app.views.api.schemas import LoginInputSchema

from ..responses import Error, Token

app = Blueprint('api.auth', __name__)


@app.route("/signin", methods=["POST"])
@inject
def signin(user_service: UserService):
    request_data = request.get_json()
    LoginInputSchema().load(request_data)
    input_data = {
        'email': request_data['email'],
        'password': request_data['password']
    }

    user = user_service.login(**input_data)
    return Token(user).response()


@app.route("/signup", methods=["POST"])
@inject
def signup(user_service: UserService):
    request_data = request.get_json()
    LoginInputSchema().load(request_data)
    input_data = {
        'email': request_data['email'],
        'password': request_data['password']
    }

    user = user_service.create_user(input_data)
    return Token(user).response()