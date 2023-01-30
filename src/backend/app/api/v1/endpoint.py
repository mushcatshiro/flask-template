from flask import jsonify, request, current_app
from backend.app.business_logic.crud import crud_todo
from backend.app.business_logic.schemas import schema_todo
from . import api_v1
from backend.app.business_logic.connection_utils import SqlAConnectionSession
# from backend.app.worker.sample_worker import sample_task


@api_v1.route('/')
def hello_world():
    current_app.logger.info("in hello_world endpoint")
    return jsonify({"response": 'hello world'})


@api_v1.route('/create/todo', methods=['POST'])
def create_todo():
    todo = schema_todo.TodoCreate().load(request.json)
    with SqlAConnectionSession(current_app.config['SQLALCHEMYDBURI']) as db:
        todo = crud_todo.create_todo(db, todo)
    current_app.logger.info(f"created {todo} in create_todo endpoint")
    return jsonify({"response": todo})


@api_v1.route('/read/todos')
def read_todos():
    with SqlAConnectionSession(current_app.config['SQLALCHEMY_DATABASE_URI']) as db:  # noqa
        todos = crud_todo.read_todos(db)
    return jsonify({"response": todos})


@api_v1.route('/read/todo/<int:todo_id>')
def read_todo(todo_id):
    with SqlAConnectionSession(current_app.config['SQLALCHEMY_DATABASE_URI']) as db:  # noqa
        todo = crud_todo.read_todo(db, todo_id)
    return jsonify({"response": todo})


@api_v1.route('/update/todo/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    updated_todo = schema_todo.TodoUpdate().load(request.json)
    with SqlAConnectionSession(current_app.config['SQLALCHEMYDBURI']) as db:
        updated_todo = crud_todo.update_todo(db, todo_id, updated_todo)
    return jsonify({"response": updated_todo})


@api_v1.route('/delete/todo/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    with SqlAConnectionSession(current_app.config['SQLALCHEMYDBURI']) as db:
        todo = crud_todo.delete_todo(db, todo_id)
    return jsonify({"response": todo})
