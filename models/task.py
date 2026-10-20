from datetime import datetime, timezone


class Task:
    def __init__(self, description, status="todo", task_id=None, created_at=None, updated_at=None):
        self.id = task_id
        self.description = description
        self.status = status
        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        self.createdAt = created_at or timestamp
        self.updatedAt = updated_at or timestamp

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt,
        }


    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        return cls(
            description=data["description"],
            status=data["status"],
            task_id=data["id"],
            created_at=data["createdAt"],
            updated_at=data["updatedAt"]
        )