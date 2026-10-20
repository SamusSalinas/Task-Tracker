import unittest
from unittest.mock import MagicMock
from models.task import Task
from services.task_service import TaskService

class TestTaskService(unittest.TestCase):
    def setUp(self):
        self.repo_mock = MagicMock()
        self.service = TaskService(repository=self.repo_mock)

    def test_add_task_assigns_correct_id(self):
        # Simulamos que el repositorio tiene una tarea con id=3
        self.repo_mock.get_all.return_value = [Task("Anterior", task_id=3)]
        
        task = self.service.add_task("Siguiente tarea")
        
        self.assertEqual(task.id, 4)
        self.repo_mock.add.assert_called_once_with(task)

    def test_update_task_success(self):
        mock_task = Task("Vieja", task_id=1)
        self.repo_mock.get_by_id.return_value = mock_task
        
        result = self.service.update_task(1, "Nueva")
        
        self.assertTrue(result)
        self.assertEqual(mock_task.description, "Nueva")
        self.repo_mock.save.assert_called_once()

    def test_mark_status_invalid(self):
        success, reason = self.service.mark_status(1, "estado_invalido")
        
        self.assertFalse(success)
        self.assertEqual(reason, "INVALID_STATUS")
        self.repo_mock.save.assert_not_called()

    def test_delete_task_not_found(self):
        self.repo_mock.get_by_id.return_value = None # Tarea no existe
        
        result = self.service.delete_task(999)
        
        self.assertFalse(result)
        self.repo_mock.remove.assert_not_called()