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
        view.incorrect_number_of_arguments("Se requiere al menos un comando. Uso: task-cli <comando> [args]")
        return
    
    match sys.argv[1:]:
        
        case ["add", description]:
            task = service.add_task(description)
            view.show_task_added(task)

        case ["delete", task_id]:
            if service.delete_task(int(task_id)):
                view.show_task_deleted()
            else:
                view.show_not_found(int(task_id))

        case ["update", task_id, new_description]:
            if service.update_task(int(task_id), new_description):
                view.show_task_updated()
            else:
                view.show_not_found(int(task_id))

        case ["mark", task_id, new_status]:
            success, reason = service.mark_status(int(task_id), new_status)
            if success:
                view.show_task_marked(new_status)
            elif reason == "INVALID_STATUS":
                view.show_invalid_status(new_status, service.VALID_STATUSES)
            else:
                view.show_not_found(int(task_id))

        case ["list"]:
            tasks, error = service.list_tasks(None)
            view.show_tasks(tasks)

        case ["list", status_filter]:
            tasks, error = service.list_tasks(status_filter)
            if error == "INVALID_STATUS":
                view.show_invalid_status(status_filter, service.VALID_STATUSES)
            else:
                view.show_tasks(tasks)

        
        case ["add" | "delete" | "update" | "mark" | "list", *rest]:
            command = sys.argv[1]
            view.incorrect_number_of_arguments(f"Número incorrecto de argumentos para el comando '{command}'.")

    
        case _:
            command = sys.argv[1]
            view.incorrect_number_of_arguments(f"Comando desconocido: '{command}'")

if __name__ == "__main__":
    main()