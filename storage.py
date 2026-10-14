from task import Task
import json


def load_tasks():
    new_task=[]
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
                new_task.append(task)
        return new_task
    except FileNotFoundError:
        return new_task

def save_tasks(new_task):
    with open("tasks.json", "w") as name1:
        json.dump([j.to_dict() for j in new_task], name1)