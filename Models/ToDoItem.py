class ToDoItem:
    def __init__(self, id, list_id, content, created_at, updated_at, deleted_at=None, is_completed=False):
        self.id = id
        self.list_id = list_id
        self.content = content
        self.created_at = created_at
        self.updated_at = updated_at
        self.deleted_at = deleted_at
        self.is_completed = is_completed

