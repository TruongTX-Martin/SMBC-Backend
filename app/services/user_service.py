import time
from typing import Dict, List, Optional

from flask import g, session
import ulid

from app.exceptions import APIResponseError, LogicError

from ..models import User
from ..repositories import UserRepository


class UserService(object):
    def __init__(self, user_repository: UserRepository, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_repository = user_repository

    def get_users(self, offset: int, limit: int) -> List[User]:
        return self.user_repository.get(offset, limit, User.id.desc())

    def get_user(self, id_: int) -> Optional[User]:
        return self.user_repository.find(id_)

    def get_user_by_email(self, email):
        return self.user_repository.first_by_filter({'email': email})

    def create_user(self, fields: Dict) -> Optional[User]:
        user_fields = {
            'email': fields['email'],
            'password': fields['password'],
        }
        check_user = self.user_repository.get_user_by_email(fields['email'])
        if check_user is not None:
            raise APIResponseError('User already exist.')

        user = self.user_repository.create(user_fields)

        return user

    def update_user(self, id_: int, fields: Dict) -> Optional[User]:
        user_fields = {'email': fields['email']}

        user = self.user_repository.find(id_)
        if user is None:
            raise APIResponseError('User Not Found.')

        user = self.user_repository.update(user, user_fields)

        return user

    def login(self, email: str, password: str) -> Optional[User]:

        user = self.user_repository.get_user_by_email(email)
        if user is None:
            raise APIResponseError('Incorrect username or password')
        elif not user.check_password(password):
            raise APIResponseError('Incorrect username or password')

        session.clear()
        session['user_id'] = user.id

        return user

    def load_logged_in_user_to_request(self, user_id: str):
        if user_id is None:
            g.user = None
        else:
            g.user = self.user_repository.find(user_id)
