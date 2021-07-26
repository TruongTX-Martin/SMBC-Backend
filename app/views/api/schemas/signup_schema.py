from marshmallow import fields

from .base_schema import BaseSchema


class SignupSchema(BaseSchema):
    email = fields.Email(required=True)
    password = fields.String(required=True)
