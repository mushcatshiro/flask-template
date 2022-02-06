from backend.app import ma
from backend.app.models.model_todo import Todo
from marshmallow import fields


class TodoSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Todo

    id = ma.auto_field()
    name = ma.auto_field()
    desc = ma.auto_field()


class TodoCreate(ma.SQLAlchemySchema):
    class Meta:
        model = Todo

    name = ma.auto_field()
    desc = ma.auto_field()


class TodoUpdate(ma.SQLAlchemySchema):
    class Meta:
        model = Todo

    name = fields.String(missing=None)
    desc = fields.String(missing=None)
