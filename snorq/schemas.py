from marshmallow import Schema, fields


class DataSchema(Schema):
    alerts = fields.Nested("AlertSchema")
    domains = fields.List(fields.Nested("DomainSchema"), required=True)


class AlertSchema(Schema):
    email = fields.Nested("EmailSchema")


class EmailSchema(Schema):
    email_from = fields.String(required=True, data_key="from")
    to = fields.List(fields.String(), required=True)
    smtp_server = fields.String(required=True)
    port = fields.Integer(required=True)
    start_tls = fields.Boolean()
    username = fields.String(required=True)
    password = fields.String(required=True)


class DomainSchema(Schema):
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
