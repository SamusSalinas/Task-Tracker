import sys
from storage.json_storage import JSONStorage
from repositories.task_repository import TaskRepository
from services.task_service import TaskService
from views.cli_view import CLIView

def main():
    storage = JSONStorage("tasks.json")
    repository = TaskRepository(loader=storage, saver=storage)
    service = TaskService(repository=repository)
    view = CLIView()

    if len(sys.argv) < 2:
        print("Usage: python main.py <command> [args...]")
        return

    command = sys.argv[1]

    if command == "add" and len(sys.argv) > 2:
        task = service.add_task(sys.argv[2])
        view.show_task_added(task)

    elif command == "delete" and len(sys.argv) > 2:
        if service.delete_task(int(sys.argv[2])):
            view.show_task_deleted()
        else:
            view.show_not_found(int(sys.argv[2]))

    elif command == "update" and len(sys.argv) > 3:
        if service.update_task(int(sys.argv[2]), sys.argv[3]):
            view.show_task_updated()
        else:
            view.show_not_found(int(sys.argv[2]))

    elif command == "mark" and len(sys.argv) > 3:
        task_id = int(sys.argv[2])
        new_status = sys.argv[3]
        success, reason = service.mark_status(task_id, new_status)
        if success:
            view.show_task_marked(new_status)
        elif reason == "INVALID_STATUS":
            view.show_invalid_status(new_status, service.VALID_STATUSES)
        else:
            view.show_not_found(task_id)

    elif command == "list":
        status_filter = sys.argv[2] if len(sys.argv) > 2 else None
        tasks, error = service.list_tasks(status_filter)
        if error == "INVALID_STATUS":
            view.show_invalid_status(status_filter, service.VALID_STATUSES)
        else:
            view.show_tasks(tasks)

if __name__ == "__main__":
    main()