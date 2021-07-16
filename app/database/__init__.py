from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from ..config import Config

if Config.FLASK_ENV == 'test':
    db = SQLAlchemy()
else:
    db = SQLAlchemy(engine_options={
        'connect_args': {
            'connect_timeout': 15  # for 15 seconds
        }
    })


def init_db(app: Flask):
    db.session.configure(info={'in_transaction': False})
    db.init_app(app)
