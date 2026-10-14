from datetime import datetime, timezone
from task import Task
from storage import save_tasks

def add_task(tasks, description):
    # Calculamos el id único
    next_id = max([task.id for task in tasks]) + 1 if tasks else 1
    new_task = Task(description=description, task_id=next_id)
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {next_id})")

def update_task(tasks, task_id, new_description):
    for task in tasks:
        if task.id == task_id:
            task.description = new_description
            task.updatedAt = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
            save_tasks(tasks)
            print("Task updated successfully!")
            return
    print(f"Task with ID {task_id} not found.")

def delete_task(tasks, task_id):
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print("Task deleted successfully!")
            return
    print(f"Task with ID {task_id} not found.")

def mark_status(tasks, task_id, new_status):
    for task in tasks:
        if task.id == task_id:
            task.status = new_status
            task.updatedAt = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
            save_tasks(tasks)
            print(f"Task marked as {new_status}!")
            return
    print(f"Task with ID {task_id} not found.")

def list_tasks(tasks, status_filter=None):
    if not tasks:
        print("No tasks found.")
        return

    # Si nos pasan un filtro (done, todo, in-progress), filtramos la lista
    if status_filter:
        tasks_to_show = [task for task in tasks if task.status == status_filter]
    else:
        tasks_to_show = tasks

    if not tasks_to_show:
        print(f"No tasks found with status: {status_filter}")
        return

    for task in tasks_to_show:
        print(f"[{task.id}] {task.description} - Status: {task.status}")