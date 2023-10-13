from marshmallow import Schema, fields, validate

class User(Schema):
    id = fields.UUID()
    username = fields.Str(required=True, validate=validate.Length(min=4, max=100))
    password = fields.Str(required=True, validate=validate.Length(min=4, max=100))
    email = fields.Email(required=True)
    created_at = fields.DateTime()