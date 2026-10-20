from abc import ABC, abstractmethod
from models.task import Task

class StorageLoadInterface(ABC):
    @abstractmethod
    def load(self) -> list[Task]:
        pass

class StorageSaveInterface(ABC):
    @abstractmethod
    def save(self, tasks: list[Task]) -> None:
        pass