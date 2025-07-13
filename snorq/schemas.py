from marshmallow import Schema, fields


class DataSchema(Schema):
    url = fields.String(required=True)
    interval = fields.Integer(required=True)
    expected = fields.Nested("ExpectedSchema")


class ExpectedSchema(Schema):
    status = fields.Integer(required=True)
    body = fields.Nested("BodySchema")
    headers = fields.Nested("HeaderSchema")


class BodySchema(Schema):
    contains = fields.List(fields.String(), data_key="in")


class HeaderSchema(Schema):
    content_type = fields.String()
