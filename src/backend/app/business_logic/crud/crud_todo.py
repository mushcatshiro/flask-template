from backend.app import db
from backend.app.schemas.schema_todo import TodoSchema
from .model_todo import Todo


def create_todo(new_todo):
    todo = Todo(**new_todo)
    db.session.add(todo)
    db.session.commit()
    db.session.refresh(todo)
    return TodoSchema().dump(todo)


def update_todo(todo_id, new_todo):
    db_todo = Todo.query.get_or_404(todo_id)
    obj_data = TodoSchema().dump(db_todo)
    for field in obj_data:
        if field in new_todo:
            setattr(db_todo, field, new_todo[field])
    db.session.add(db_todo)
    db.session.commit()
    db.session.refresh(db_todo)
    return TodoSchema().dump(db_todo)


def read_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    return TodoSchema().dump(todo)


def read_todos():
    todos = Todo.query.all()
    return TodoSchema(many=True).dump(todos)


def delete_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return TodoSchema().dump(todo)
