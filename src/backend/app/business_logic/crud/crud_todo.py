from ..schemas import TodoSchema
from ..models import Todo
from ..custom_exceptions import ResourceNotFoundError


def create_todo(db, new_todo):
    todo = Todo(**new_todo)
    db.session.add(todo)
    db.session.commit()
    db.session.refresh(todo)
    return TodoSchema().dump(todo)


def update_todo(db, todo_id, new_todo):
    db_todo = Todo.query.get_or_404(todo_id)
    obj_data = TodoSchema().dump(db_todo)
    for field in obj_data:
        if field in new_todo:
            setattr(db_todo, field, new_todo[field])
    db.session.add(db_todo)
    db.session.commit()
    db.session.refresh(db_todo)
    return TodoSchema().dump(db_todo)


def read_todo(db, todo_id):
    todo = db.conn.query(Todo).filter(Todo.id == todo_id).first()
    if todo is None:
        raise ResourceNotFoundError(
            message=f'id {todo_id} is not found',
            err_message=f'id {todo_id} is not found in db',
            status_code=404
        )
    return TodoSchema().dump(todo)


def read_todos(db):
    todos = db.conn.query(Todo).all()
    return TodoSchema(many=True).dump(todos)


def delete_todo(db, todo_id):
    todo = Todo.query.get_or_404(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return TodoSchema().dump(todo)
