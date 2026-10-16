import unittest
from unittest.mock import patch
from task import Task
from task_manager import add_task, delete_task, mark_status, update_task

class TestTaskManager(unittest.TestCase):

    @patch("task_manager.save_tasks")
    def test_add_task_to_empty_list(self, mock_save):
        tasks = []
        add_task(tasks, "Primera tarea")
        
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].id, 1)
        self.assertEqual(tasks[0].description, "Primera tarea")
        mock_save.assert_called_once()

    @patch("task_manager.save_tasks")
    def test_add_task_to_empty_list(self, mock_save):
        tasks=[Task("Primera Tarea", task_id=3)]
        add_task(tasks, "Segunda tarea")

        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[1].id, 4)
        mock_save.assert_called_once()

    @patch("task_manager.save_tasks")
    def test_update_task(self, mock_save):
        tasks = [Task("Vieja descripción", task_id=1)]
        update_task(tasks, 1, "Nueva descripción")

        self.assertEqual(tasks[0].description, "Nueva descripción")
        mock_save.assert_called_once()

    @patch("task_manager.save_tasks")
    def test_delete_task(self, mock_save):
        tasks = [Task("Tarea a borrar", task_id=1)]
        delete_task(tasks, 1)

        self.assertEqual(tasks, [])
        mock_save.assert_called_once()

    @patch("task_manager.save_tasks")
    def test_mark_status(self, mock_save):
        tasks = [Task("Tarea pendiente", task_id=1, status="todo")]
        mark_status(tasks, 1, "done")

        self.assertEqual(tasks[0].status, "done")
        mock_save.assert_called_once()

    @patch("task_manager.save_tasks")
    def test_mark_status_invalid(self, mock_save):
        tasks = [Task("Tarea pendiente", task_id=1, status="todo")]
        mark_status(tasks, 1, "estado_invalido")

        self.assertEqual(tasks[0].status, "todo")
        mock_save.assert_not_called()