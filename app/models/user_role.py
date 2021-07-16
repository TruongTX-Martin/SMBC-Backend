from datetime import datetime

from sqlalchemy import func
from sqlalchemy.dialects import sqlite

from ..database import db


class UserRole(db.Model):
    __tablename__ = 'user_roles'

    id = db.Column('id',
                   db.BigInteger().with_variant(sqlite.INTEGER(), 'sqlite'),
                   primary_key=True)
    user_id = db.Column('user_id', db.BigInteger, nullable=False)
    role = db.Column('role', db.String(255), nullable=False)

    created_at = db.Column('created_at',
                           db.TIMESTAMP,
                           default=datetime.utcnow,
                           server_default=func.current_timestamp(),
                           nullable=False)
    updated_at = db.Column('updated_at',
                           db.TIMESTAMP,
                           default=datetime.utcnow,
                           onupdate=datetime.utcnow,
                           server_default=func.current_timestamp(),
                           nullable=False)

    def __repr__(self):
        return "<{name} '{id}'>".format(name=self.__class__.__name__,
                                        id=self.id)
