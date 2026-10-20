import json
from interfaces.storage import StorageLoadInterface, StorageSaveInterface
from models.task import Task

class JSONStorage(StorageLoadInterface, StorageSaveInterface):
    def __init__(self, file_path: str = "tasks.json"):
        self.file_path = file_path

    def load(self) -> list[Task]:
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                tasks_data = json.load(file)
                return [Task.from_dict(data) for data in tasks_data]
        except FileNotFoundError:
            return []

    def save(self, tasks: list[Task]) -> None:
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump([task.to_dict() for task in tasks], file, indent=2)