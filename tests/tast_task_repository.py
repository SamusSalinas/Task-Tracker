import unittest
from unittest.mock import MagicMock
from models.task import Task
from repositories.task_repository import TaskRepository

class TestTaskRepository(unittest.TestCase):
    def setUp(self):
        # Mocks para las interfaces
        self.loader_mock = MagicMock()
        self.saver_mock = MagicMock()
        
        # Simulamos que el loader devuelve 1 tarea al inicializar
        self.loader_mock.load.return_value = [Task("Tarea inicial", task_id=1)]
        
        # Inyectamos dependencias
        self.repo = TaskRepository(loader=self.loader_mock, saver=self.saver_mock)

    def test_get_all(self):
        self.assertEqual(len(self.repo.get_all()), 1)

    def test_add_saves_data(self):
        nueva_tarea = Task("Nueva", task_id=2)
        self.repo.add(nueva_tarea)
        
        self.assertEqual(len(self.repo.get_all()), 2)
        self.saver_mock.save.assert_called_once() # Verifica que delegó el guardado

    def test_remove_saves_data(self):
        tarea = self.repo.get_by_id(1)
        self.repo.remove(tarea)
        
        self.assertEqual(len(self.repo.get_all()), 0)
        self.saver_mock.save.assert_called_once()