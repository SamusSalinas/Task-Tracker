from interfaces.storage import StorageLoadInterface, StorageSaveInterface
from models.task import Task

class TaskRepository:
    def __init__(self, loader: StorageLoadInterface, saver: StorageSaveInterface):
        self._loader = loader
        self._saver = saver
        self._tasks: list[Task] = self._loader.load()

    def get_all(self) -> list[Task]:
        return self._tasks

    def get_by_id(self, task_id: int) -> Task | None:
        return next((task for task in self._tasks if task.id == task_id), None)

    def add(self, task: Task) -> None:
        self._tasks.append(task)
        self.save()

    def remove(self, task: Task) -> None:
        self._tasks.remove(task)
        self.save()

    def save(self) -> None:
        self._saver.save(self._tasks)