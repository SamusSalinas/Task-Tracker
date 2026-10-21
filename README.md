# Task Tracker CLI

Una aplicación de línea de comandos (CLI) modular y robusta para la gestión de tareas, construida en **Python 3**. Este proyecto destaca no solo por su funcionalidad, sino por su diseño interno, aplicando fuertemente principios de **Clean Architecture**, **SOLID**, y **persistencia de datos en JSON**.

> **Nota:** Esta es una implementación y solución para el proyecto [Task Tracker](https://roadmap.sh/projects/task-tracker) propuesto en **roadmap.sh**.

## Compatibilidad con Python

La CI está configurada para compilar todos los archivos Python, ejecutar las pruebas unitarias y realizar una prueba básica de la CLI con Python 3.12 y 3.15. El proyecto no declara una versión mínima estricta de Python.

Instala las dependencias antes de ejecutar la aplicación:

```bash
python -m pip install -r requirements.txt
```

## Características Principales

* **Gestión CRUD Completa**: Creación, actualización, eliminación y listado de tareas.
* **Control de Estados**: Actualización fluida del estado de tareas (`todo`, `in-progress`, `done`).
* **Filtrado**: Filtrado de tareas por estado directamente desde la línea de comandos.
* **Validación de Datos**: Validación centralizada de entradas de comandos y estados (`VALID_STATUSES`).
* **Persistencia de Datos**: Almacenamiento local automático mediante archivos JSON (`json.load` / `json.dump`).
* **Arquitectura Limpia y SOLID**: Separación estricta de responsabilidades (Modelos, Interfaces, Repositorios, Servicios y Vistas) con Inyección de Dependencias.
* **Pruebas Unitarias**: Suite de pruebas robusta implementada con `unittest` y `MagicMock` garantizando la fiabilidad del código.

## Guía de Comandos para task-cli

### 1. Agregar una tarea

Añade una nueva tarea a la lista (el estado inicial por defecto será `todo`).

```bash
python main.py add "Comprar leche y pan"
```

### 2. Actualizar la descripción

Modifica la descripción de una tarea existente buscando por su ID.

```bash
python main.py update 1 "Comprar leche, pan y café"
```

### 3. Cambiar el estado de una tarea

Actualiza el estado de una tarea indicando su ID y el nuevo estado (`todo`, `in-progress` o `done`).

* Marcar en progreso:

```bash
python main.py mark 1 in-progress
```

* Marcar como completada:

```bash
python main.py mark 1 done
```

### 4. Eliminar una tarea

Elimina una tarea de la lista mediante su ID.

```bash
python main.py delete 1
```

### 5. Listar tareas

Muestra las tareas guardadas. Puedes ver todas o filtrar según su estado.

* Listar TODAS las tareas:

```bash
python main.py list
```

* Filtrar por estado específico:

```bash
python main.py list done
python main.py list todo
python main.py list in-progress
```

## Ejecución de Pruebas Automáticas

El proyecto incluye una suite de pruebas unitarias que validan el correcto funcionamiento de las reglas de negocio y el almacenamiento sin modificar los datos reales del usuario.

Para ejecutar las pruebas, utiliza el siguiente comando desde la raíz del proyecto:

```bash
python -m unittest discover -s tests
```