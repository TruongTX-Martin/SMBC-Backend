from marshmallow import fields

from .base_schema import BaseSchema


class CheckPasswordTokenSchema(BaseSchema):
    token = fields.Str(required=True)
