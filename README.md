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

https://roadmap.sh/projects/task-tracker