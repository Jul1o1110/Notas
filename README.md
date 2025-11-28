# Sistema de Gestión de Notas Estudiantiles

Este es un proyecto simple desarrollado en Python para gestionar notas, cumpliendo con los requisitos de modularización, uso de estructuras de datos (Diccionarios/Listas) y control de flujo (Ciclo while).

---

## Requisitos Funcionales

El sistema incluye:

1.  **Menú Interactivo:** Implementación de un ciclo `while` para las opciones del menú.
2.  **Uso de Diccionarios y Listas:** Se utiliza un **Diccionario** (`datos_estudiantes`) donde la llave es el nombre del estudiante y el valor es una **Lista** que almacena sus notas.
3.  **Uso de Funciones:** La lógica está separada en las funciones `registrar_ingreso()`, `registrar_nota()`, y `ver_promedio()`.

---

## Estructura del Proyecto (Modularización)

El código se divide en dos archivos para mejorar la organización:

| `main.py` | Contiene el menú (`mostrar_menu`) y la ejecución principal (`main`). |
| `logica.py` | Contiene el diccionario `datos_estudiantes` y las funciones de procesamiento. |

---

## Cómo Ejecutar

1.  Clonar el repositorio.
2.  Ejecutar la aplicación desde la terminal: `python main.py`

---

## Requerimientos de Versionamiento (Git)

El proyecto debe cumplir con:

1.  **Repositorio Git Iniciado.**
2.  **Estrategia de Ramas:** Existencia de al menos tres ramas: `main`, `feature/notas`, y `feature/aprueba`.
3.  **Historial de Commits:** Historial limpio y descriptivo.

### Comandos Clave

* Crear rama: `git checkout -b nombre-rama`
* Commit: `git commit -m "Descripción"`
* Subir todo a GitHub: `git push --all origin`