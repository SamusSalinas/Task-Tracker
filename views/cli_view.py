from models.task import Task

class CLIView:
    @staticmethod
    def show_task_added(task: Task) -> None:
        print(f"Task added successfully (ID: {task.id})")

    @staticmethod
    def show_task_updated() -> None:
        print("Task updated successfully!")

    @staticmethod
    def show_task_deleted() -> None:
        print("Task deleted successfully!")

    @staticmethod
    def show_task_marked(status: str) -> None:
        print(f"Task marked as {status}!")

    @staticmethod
    def show_not_found(task_id: int) -> None:
        print(f"Task with ID {task_id} not found.")

    @staticmethod
    def show_invalid_status(status: str, valid_statuses: list[str]) -> None:
        print(f"Invalid status: '{status}'. Valid statuses are: {', '.join(valid_statuses)}")

    @staticmethod
    def show_tasks(tasks: list[Task]) -> None:
        if not tasks:
            print("No tasks found.")
            return
        for task in tasks:
            print(f"[{task.id}] {task.description} - Status: {task.status}")