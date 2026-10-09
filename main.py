from datetime import datetime, timezone
import sys
import json
from task import Task

tasks = []

def load_tasks():
    try:
        with open("tasks.json", "r") as name1:
            tasks_data = json.load(name1)
            for task_data in tasks_data:
                task = Task(
                    task_data["description"],
                    task_data["status"],
                    task_data["id"],
                    task_data["createdAt"],
                    task_data["updatedAt"]
                )
                tasks.append(task)
    except FileNotFoundError:
        pass

def save_tasks():
    with open("tasks.json", "w") as name1:
        json.dump([j.to_dict() for j in tasks], name1)

def add_task():
    id = max([task.task_id for task in tasks]) + 1 if tasks else 1
    desc = sys.argv[2]
    task = Task(desc, "todo", id)
    tasks.append(task)
    save_tasks()
    print("Task added!")

def show_tasks():
    if not tasks:
        print("There is no task.")
        return
    for l, task in enumerate(tasks, start=1):
        print(f"{l}. {task.title} - {task.description}")

def update_task():
    if len(sys.argv) < 4:
        print("Ingresa el ID de la tarea y el nuevo estado.")
        return
    task_id = int(sys.argv[2])
    new_description = sys.argv[3]
    for task in tasks:
        if task.id == task_id:
            task.description = new_description
            task.updatedAt = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
            save_tasks()
            print("Task updated!")
            
def delete_task():
    if len(sys.argv)<3:
        print("Please provide the ID of the task to delete.")
        return
    task_id = int(sys.argv[2])
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            save_tasks()
            print("Task deleted!")
            return

load_tasks()

if sys.argv[1] == "add":
    add_task()
elif sys.argv[1] == "show":
    show_tasks()
elif sys.argv[1] == "update":
    update_task()
elif sys.argv[1] == "save":
    save_tasks()
    
else:
    print("Wrong choice.")

sys.argv[0] = "main.py"
sys.argv[1] = "add"
sys.argv[2] = "Buy groceries"
