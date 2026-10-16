import unittest
from unittest.mock import patch, mock_open
import json
from task import Task
from storage import save_tasks, load_tasks

class TestStorage(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open)
    def test_save_tasks(self, mock_file):
        tasks = [Task("Tarea de prueba", task_id=1)]
        save_tasks(tasks)
        
        # Verificamos que 'open' fue llamado para escribir el archivo
        mock_file.assert_called_once_with("tasks.json", "w")
        mock_file().write.assert_called()

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_load_tasks_file_not_found(self, mock_file):
        # Invocamos la función
        tasks = load_tasks()
        self.assertEqual(tasks, [])