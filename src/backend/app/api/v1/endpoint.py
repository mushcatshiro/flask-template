from flask import jsonify, request, current_app
from backend.app.crud import crud_todo
from backend.app.schemas import schema_todo
from backend.app.api.v1 import api
# from backend.app.worker.sample_worker import sample_task


@api.route('/')
def hello_world():
    current_app.logger.info("in hello_world endpoint")
    return jsonify({"response": 'hello world'})


@api.route('/create/todo', methods=['POST'])
def create_todo():
    todo = schema_todo.TodoCreate().load(request.json)
    todo = crud_todo.create_todo(todo)
    current_app.logger.info(f"created {todo} in create_todo endpoint")
    return jsonify({"response": todo})


@api.route('/read/todos')
def read_todos():
    todos = crud_todo.read_todos()
    return jsonify({"response": todos})


@api.route('/read/todo/<int:todo_id>')
def read_todo(todo_id):
    todo = crud_todo.read_todo(todo_id)
    return jsonify({"response": todo})


@api.route('/update/todo/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    updated_todo = schema_todo.TodoUpdate().load(request.json)
    updated_todo = crud_todo.update_todo(todo_id, updated_todo)
    return jsonify({"response": updated_todo})


@api.route('/delete/todo/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todo = crud_todo.delete_todo(todo_id)
    return jsonify({"response": todo})
