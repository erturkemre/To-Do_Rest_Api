class ToDoList:
    def __init__(self, id, name, created_at, updated_at, deleted_at=None, completion_percentage=0):
        self.id = id
        self.name = name
        self.created_at = created_at
        self.updated_at = updated_at
        self.deleted_at = deleted_at
        self.completion_percentage = completion_percentage
