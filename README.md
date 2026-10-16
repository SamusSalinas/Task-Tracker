# 📝 Task Tracker CLI

Una aplicación de línea de comandos (CLI) modular y robusta para la gestión de tareas, construida en **Python 3** aplicando principios de **Clean Code**, **arquitectura modular** y **persistencia de datos en JSON**.

## Compatibilidad con Python

La CI está configurada para compilar todos los archivos Python y ejecutar una prueba básica de la CLI con Python 3.12 y 3.15. El proyecto no declara una versión mínima de Python.

---

## 🎯 Características Principal

* ➕ **Gestión CRUD Completa**: Creación, actualización, eliminación y listado de tareas.
* 🔄 **Control de Estados**: Actualización del estado de tareas (`todo`, `in-progress`, `done`).
* 🔍 **Filtrado**: Filtrado de tareas por estado desde la línea de comandos.
* 🛡️ **Validación de Datos**: Validación de entrada de comandos y estados centralizados (`VALID_STATUSES`).
* 💾 **Persistencia de Datos**: Almacenamiento local mediante archivos JSON (`json.load` / `json.dump`).

---

## 🏗️ Arquitectura del Proyecto

El proyecto está estructurado siguiendo el principio de **separación de responsabilidades** (Separation of Concerns):

```text
task-cli/
├── task.py          # 📄 Modelo de datos (Clase Task y serialización to_dict)
├── storage.py       # 💾 Módulo de persistencia (Lectura y escritura en JSON)
├── task_manager.py  # 🧠 Lógica de negocio y validación de estados
├── main.py          # 🖥️ Punto de entrada CLI y manejo de sys.argv
└── tasks.json       # 📦 Archivo de almacenamiento de datos