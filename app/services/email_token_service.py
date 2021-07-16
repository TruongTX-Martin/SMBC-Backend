from datetime import datetime, timedelta

import jwt

from app.config import Config
from app.exceptions import APIResponseError
from app.models import EmailToken
from app.repositories import EmailTokenRepository


class EmailTokenService(object):
    def __init__(self, email_token_repository: EmailTokenRepository, *args,
                 **kwargs):
        super().__init__(*args, **kwargs)
        self.email_token_repository = email_token_repository

    def validate(self, token):
        try:
            jwt.decode(token, Config.SECRET_KEY, algorithms='HS256')
            return True
        except AttributeError:
            raise APIResponseError('Token does not exist.')
        except jwt.DecodeError:
            raise APIResponseError('Token is invalid.')
        except jwt.ExpiredSignatureError as e:
            raise APIResponseError('Token is expired.')

    def get_email_token_by_token(self, token: str) -> EmailToken:
        return self.email_token_repository.first_by_filter({'token': token})

    def delete(self, email_token: EmailToken):
        return self.email_token_repository.delete(email_token)

    def create_token(self, email, timeout=None) -> str:
        self.email_token_repository.delete_by_filter({
            'email': email,
        })

        if not timeout:
            timeout = Config.TOKEN_EXPIRED_IN_DAYS

        exp = datetime.utcnow() + timedelta(days=timeout)
        encoded = jwt.encode({
            'id': email,
            'exp': exp
        },
                             Config.SECRET_KEY,
                             algorithm='HS256')
        token = encoded.decode('utf-8')

        self.email_token_repository.create({
            'token': token,
            'email': email,
        })

        return token
