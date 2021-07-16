import datetime

from sqlalchemy import func
from sqlalchemy.dialects import sqlite

from ..database import db


class EmailToken(db.Model):
    __tablename__ = 'email_tokens'

    id = db.Column('id',
                   db.BigInteger().with_variant(sqlite.INTEGER(), 'sqlite'),
                   primary_key=True)
    email = db.Column('email', db.String(255), nullable=False)
    token = db.Column('token', db.String(255), nullable=False)

    created_at = db.Column('created_at',
                           db.TIMESTAMP,
                           default=datetime.datetime.utcnow,
                           server_default=func.current_timestamp(),
                           nullable=False)
    updated_at = db.Column('updated_at',
                           db.TIMESTAMP,
                           onupdate=datetime.datetime.utcnow,
                           default=datetime.datetime.utcnow,
                           server_default=func.current_timestamp(),
                           nullable=False)

    def __repr__(self):
        return "<{name} '{id}'>".format(name=self.__class__.__name__,
                                        id=self.id)
