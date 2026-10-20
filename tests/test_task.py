import unittest
from unittest.mock import patch, mock_open
from models.task import Task
from storage.json_storage import JSONStorage

class TestJSONStorage(unittest.TestCase):
    def setUp(self):
        self.storage = JSONStorage("tasks.json")

    @patch("builtins.open", new_callable=mock_open)
    def test_save_tasks(self, mock_file):
        tasks = [Task("Tarea de prueba", task_id=1)]
        self.storage.save(tasks)
        
        mock_file.assert_called_once_with("tasks.json", "w", encoding="utf-8")
        mock_file().write.assert_called()

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_load_tasks_file_not_found(self, mock_file):
        tasks = self.storage.load()
        self.assertEqual(tasks, [])