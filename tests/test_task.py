import unittest
from task import Task

class TestTask(unittest.TestCase):

    def test_task_creation_defaults(self):
        # Creamos una tarea con lo mínimo
        task = Task(description="Comprar leche", task_id=1)
        
        # Verificamos valores
        self.assertEqual(task.id, 1)
        self.assertEqual(task.description, "Comprar leche")
        self.assertEqual(task.status, "todo")
        self.assertIsNotNone(task.createdAt)
        self.assertIsNotNone(task.updatedAt)

    def test_task_to_dict(self):
        task = Task(description="Estudiar Python", task_id=2)
        task_dict = task.to_dict()
        
        # ¿Qué aserciones deberíamos hacer aquí?
        self.assertEqual(task_dict['id'],2)
        self.assertEqual(task_dict['description'], "Estudiar Python")
        self.assertEqual(task_dict['status'], "todo")
        self.assertIn('createdAt', task_dict)
        self.assertIn('updatedAt', task_dict)
        