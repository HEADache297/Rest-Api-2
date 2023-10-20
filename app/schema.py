from marshmallow import Schema, fields, validate

class User(Schema):
    id = fields.UUID()
    username = fields.Str(required=True, validate=validate.Regexp("^(?=.*[a-z])(?=.*[A-Z])[a-zA-Z]{4,}$", error = "Username must only cantain [a-z][A-Z]"))
    password = fields.Str(required=True, validate=validate.Regexp("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&*!])[a-zA-Z\d@#$%^&*!]{8,}$", error="Password must contain a-z A-z 0-9 @!@$#%^*"))
    email = fields.Email(required=True, validate=validate.Regexp("[a-zA-Z0-9]+@[a-z]{2,}\.[a-z]{2,}", error="Email should lokk like example@example.com"))
    created_at = fields.DateTime()