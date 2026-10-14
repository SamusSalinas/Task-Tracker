import sys
from task_manager import add_task, update_task, delete_task, mark_status, list_tasks
from storage import load_tasks

tasks = load_tasks()

command = sys.argv[1] if len(sys.argv) > 1 else None

if command == "add":
    description = sys.argv[2]
    add_task(tasks, description)

elif command == "delete":
    task_id = int(sys.argv[2])
    delete_task(tasks, task_id)

elif command == "update":
    task_id = int(sys.argv[2])
    new_description = sys.argv[3]
    update_task(tasks, task_id, new_description)

elif command == "mark":
    task_id = int(sys.argv[2])
    new_status = sys.argv[3]
    mark_status(tasks, task_id, new_status)

elif command == "list":
    if len(sys.argv) > 2:
        status_filter = sys.argv[2]
        list_tasks(tasks, status_filter)
    else:
        list_tasks(tasks)

else:
    print("Invalid command. Available commands: add, delete, update, mark, list")