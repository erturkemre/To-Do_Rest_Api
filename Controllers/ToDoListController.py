from flask import request, jsonify
from datetime import datetime
from Models import ToDoList, ToDoItem


class ToDoListController(ToDoList):
    def create_todo_list(self, name, user_id):
        todo_list = ToDoList(name=name, id=user_id)
        todo_list.save()
        return todo_list.to_dict()

    def get_todo_list(self, id):
        todo_list = ToDoList(id=id)
        todo_list.get()
        if not todo_list:
            return None

        return todo_list.to_dict()

