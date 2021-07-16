from marshmallow import fields, validate, validates

from app.exceptions import ParameterError
from app.helpers import StringHelper

from .base_schema import BaseSchema


class ResetPasswordSchema(BaseSchema):
    token = fields.Str(required=True)
    password = fields.Str(required=True,
                          validate=validate.Length(max=32, min=6))

    @validates('password')
    def validate_password(self, password):
        message = 'Password must contain between 8 and 30 characters,' \
                  ' at least one capital letter,' \
                  ' at least one numeric digit,' \
                  ' and at least one special character (such as $ or !)'

        if not StringHelper.is_validate_password(password):
            raise ParameterError({'password': [message]})
