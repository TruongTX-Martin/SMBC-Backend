from marshmallow import fields

from .base_schema import BaseSchema


class ForgotPasswordSchema(BaseSchema):
    email = fields.Email(required=True)
