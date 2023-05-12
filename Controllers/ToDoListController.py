from flask import request, jsonify
from datetime import datetime
from Models import ToDoList


class ToDoListController(ToDoList):
    def create_todo_list(self,id, name):
        todo_list = ToDoList(name=name, id=id)
        todo_list.save()
        return todo_list.to_dict()

    def get_todo_list(self, id):
        todo_list = ToDoList(id=id)
        todo_list.get(id)
        if not todo_list:
            return None
        todo_list.save()
        return todo_list.to_dict()

    def update_todo_list(self, id, updated_at):
        todo_list = ToDoList(id=id, updated_at=updated_at)
        if not todo_list:
            return None
        todo_list.updated_at = datetime.now()
        todo_list.save()
        return todo_list.to_dict()

    def delete_todo_list(self, id, deleted_at):
        todo_list = ToDoList(id=id, deleted_at=deleted_at)
        todo_list.deleted_at = datetime.now()
        todo_list.save()

        return todo_list.to_dict()



