from datetime import datetime, timezone
from models.task import Task
from repositories.task_repository import TaskRepository

class TaskService:
    VALID_STATUSES = ["todo", "in-progress", "done"]

    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def add_task(self, description: str) -> Task:
        tasks = self.repository.get_all()
        next_id = max([t.id for t in tasks], default=0) + 1
        new_task = Task(description=description, task_id=next_id)
        self.repository.add(new_task)
        return new_task

    def update_task(self, task_id: int, new_description: str) -> bool:
        task = self.repository.get_by_id(task_id)
        if not task:
            return False
        
        task.description = new_description
        task.updatedAt = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        self.repository.save()
        return True

    def delete_task(self, task_id: int) -> bool:
        task = self.repository.get_by_id(task_id)
        if not task:
            return False
        
        self.repository.remove(task)
        return True

    def mark_status(self, task_id: int, new_status: str) -> tuple[bool, str]:
        if new_status not in self.VALID_STATUSES:
            return False, "INVALID_STATUS"
        
        task = self.repository.get_by_id(task_id)
        if not task:
            return False, "NOT_FOUND"

        task.status = new_status
        task.updatedAt = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        self.repository.save()
        return True, "SUCCESS"

    def list_tasks(self, status_filter: str = None) -> tuple[list[Task], str | None]:
        if status_filter and status_filter not in self.VALID_STATUSES:
            return [], "INVALID_STATUS"

        tasks = self.repository.get_all()
        if status_filter:
            tasks = [t for t in tasks if t.status == status_filter]

        return tasks, None