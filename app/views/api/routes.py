from flask import Blueprint, Flask, redirect, request

from .controllers import me_controller


def build_routes(app: Flask) -> None:
    app.register_blueprint(me_controller, url_prefix='/api/v1/me')
