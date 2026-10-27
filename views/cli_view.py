from rich import box
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from models.task import Task

console = Console()

class CLIView:

    @staticmethod
    def incorrect_number_of_arguments(message: str) -> None:
        console.print(Panel(f"[bold red]Error:[/bold red] {message}", border_style="red", expand=False))

    @staticmethod
    def show_task_added(task: Task) -> None:
        console.print(Panel(f"[bold green]Tarea agregada con éxito![/bold green]\nID asignado: [cyan]{task.id}[/cyan]", 
                            title="Nueva Tarea", border_style="green", expand=False))

    @staticmethod
    def show_task_updated() -> None:
        console.print("[bold blue]Tarea actualizada correctamente.[/bold blue]")

    @staticmethod
    def show_task_deleted() -> None:
        console.print("[bold red]Tarea eliminada permanentemente.[/bold red]")

    @staticmethod
    def show_task_marked(status: str) -> None:
        color = "yellow" if status == "in-progress" else "green"
        console.print(Panel(f"[{color}]Estado de la tarea actualizado a '{status}'![/{color}]", 
                            title="Actualización de Tarea", border_style=color, expand=False))

    @staticmethod
    def show_not_found(task_id: int) -> None:
        console.print(f"[bold red]Error:[/bold red] No se encontró ninguna tarea con el ID [yellow]{task_id}[/yellow].")

    @staticmethod
    def show_invalid_status(status: str, valid_statuses: list[str]) -> None:
        console.print(f"[bold red]Estado inválido:[/bold red] '{status}'.")
        console.print(f"Los estados permitidos son: [cyan]{', '.join(valid_statuses)}[/cyan]")

    @staticmethod
    def show_tasks(tasks: list[Task]) -> None:
        if not tasks:
            console.print(Panel("[yellow]No hay tareas para mostrar.[/yellow]", expand=False))
            return

        # Crear una tabla visual
        table = Table(title="Lista de Tareas", box=box.ROUNDED, show_header=True, header_style="bold magenta",)
        
        table.add_column("ID", style="cyan", justify="center", width=4)
        table.add_column("Descripción", style="white")
        table.add_column("Estado", justify="center", width=15)
        table.add_column("Creación", style="dim", justify="center", width=12)
        table.add_column("Última Actualización", style="dim", justify="center")

        for task in tasks:
            if task.status == "todo":
                status_formatted = "[red]Pendiente[/red]"
            elif task.status == "in-progress":
                status_formatted = "[yellow]En Progreso[/yellow]"
            else:
                status_formatted = "[green]Completada[/green]"

            date_str = task.updatedAt.split("T")[0]
            created_date_str = task.createdAt.split("T")[0]

            table.add_row(str(task.id), task.description, status_formatted, created_date_str, date_str)

        console.print(table)