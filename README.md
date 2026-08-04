# 🐍 Python - Mes 2: Desarrollo Backend con FastAPI & Pydantic

¡Bienvenido al segundo mes de mi plan de estudio autodidacta de 180 días! Después de dominar las bases del lenguaje y las pruebas de software en el Mes 1, este bloque está completamente enfocado en la construcción de servicios backend modernos, ágiles y listos para producción.

El objetivo principal de este mes es adquirir las habilidades necesarias para construir APIs REST robustas y prepararme para ingresar al mercado laboral en noviembre de 2026.

## 🎯 Objetivos de este Mes
* Comprender y aplicar la arquitectura Cliente-Servidor y el estándar REST.
* Dominar el framework **FastAPI** para la creación de endpoints eficientes.
* Implementar validación de datos estricta utilizando **Pydantic**.
* Conectar aplicaciones a bases de datos y gestionar operaciones CRUD.
* Desplegar y documentar APIs bajo estándares profesionales.

## 📅 Estructura del Bloque (Días 31-40)
* **Día 31:** Fundamentos de APIs REST, métodos HTTP e instalación del entorno en Mac. Creación de los primeros endpoints (`/`, `/salud`, `/empleado`) y uso de Swagger UI.
* **Día 32 - 40:** *En desarrollo... (Validación de esquemas, Query Parameters, Path Parameters y manejo de estados).*

## 🛠️ Tecnologías y Herramientas utilizadas
* **Lenguaje:** Python 3
* **Framework:** FastAPI
* **Servidor ASGI:** Uvicorn
* **Editor de Código:** Visual Studio Code
* **Control de Versiones:** Git & GitHub

---
_Proceso de aprendizaje guiado con auditorías de código diarias para asegurar la calidad del software._

---

# 🐍 Python - Mes 2: Desarrollo Backend con FastAPI & Pydantic


## 💡 Conceptos Clave Aprendidos en el Día 32
1. **Path Parameters (Parámetros de Ruta):**
   * Utilizados para identificar recursos únicos en la URL (ejemplo: `/empleados/3`).
   * Validación automática de tipos mediante type hints (`empleado_id: int`). Si el cliente envía un tipo de dato incorrecto, FastAPI retorna un error 422 de forma automática.
2. **Query Parameters (Parámetros de Consulta):**
   * Parámetros opcionales al final de la URL precedidos por `?` para filtrar o buscar (ejemplo: `/empleados?cargo=Backend`).
3. **Depuración y Lógica de Bucles en Python:**
   * Importancia de la indentación adecuada en los retornos dentro de un bucle `for`. Evitar retornos prematuros dentro del scope del bloque para garantizar el recorrido completo de la estructura de datos.

## 🛠️ Tecnologías y Herramientas utilizadas
* **Lenguaje:** Python 3
* **Framework:** FastAPI
* **Servidor ASGI:** Uvicorn
* **Editor de Código:** Visual Studio Code
* **Control de Versiones:** Git & GitHub

---
_Proceso de aprendizaje guiado con auditorías de código diarias para asegurar la calidad del software._

---

## 💡 Conceptos Clave Aprendidos en el Día 33
1. **Método HTTP POST:**
   * Utilizado para enviar información al servidor y crear nuevos recursos.
   * Transmisión de datos en el cuerpo de la solicitud (*Request Body*) utilizando el formato `application/json`.
2. **Estructura y Validación de JSON:**
   * Sensibilidad de la sintaxis JSON (comillas dobles, llaves y comas). FastAPI retorna automáticamente un código **422 Unprocessable Content** en caso de JSON mal formado.
3. **Manejo de Estado en Memoria:**
   * Modificación de estructuras de datos persistidas durante el ciclo de vida de la aplicación mediante `.append()`.

## 🛠️ Tecnologías y Herramientas utilizadas
* **Lenguaje:** Python 3
* **Framework:** FastAPI
* **Servidor ASGI:** Uvicorn
* **Editor de Código:** Visual Studio Code
* **Control de Versiones:** Git & GitHub

_Proceso de aprendizaje guiado con auditorías de código diarias para asegurar la calidad del software._

---

## 💡 Conceptos Clave Aprendidos en el Día 34
1. **Pydantic v2 Schemas (`BaseModel`):**
   * Definición de contratos de entrada tipados (`id: int`, `nombre: str`, `cargo: str`) que protegen la API contra datos corruptos.
   * Generación automática de esquemas en la documentación Swagger UI / OpenAPI.
2. **Método `.model_dump()`:**
   * Reemplazo moderno y vigente de `.dict()` (deprecado en Pydantic v1) para convertir modelos de Pydantic a diccionarios nativos de Python.
3. **Manejo de Errores 422 (Unprocessable Content):**
   * Intercepción de datos inválidos en la capa de transporte HTTP antes de ejecutar la lógica de negocio.

## 🛠️ Tecnologías y Herramientas utilizadas
* **Lenguaje:** Python 3
* **Framework:** FastAPI
* **Validación:** Pydantic v2
* **Servidor ASGI:** Uvicorn
* **Editor de Código:** Visual Studio Code
* **Control de Versiones:** Git & GitHub

---
_Proceso de aprendizaje guiado con auditorías de código diarias para asegurar la calidad del software._

---

## 💡 Conceptos Clave Aprendidos en el Día 35
1. **Códigos HTTP Semánticos:**
   * Configuración de `status.HTTP_201_CREATED` directamente en el decorador del endpoint para confirmar la creación limpia de un recurso.
2. **Excepciones de Control (`HTTPException`):**
   * Interrupción explícita de la petición con `raise HTTPException` cuando un recurso solicitado no existe.
   * Modificación real de las cabeceras HTTP del servidor enviando un código **404 Not Found** en lugar de retornar un JSON con un mensaje manual.

## 🛠️ Tecnologías y Herramientas utilizadas
* **Lenguaje:** Python 3
* **Framework:** FastAPI (`HTTPException`, `status`)
* **Validación:** Pydantic v2
* **Servidor ASGI:** Uvicorn
* **Control de Versiones:** Git & GitHub

---
_Proceso de aprendizaje guiado con auditorías de código diarias para asegurar la calidad del software._

## 💡 Conceptos Clave Aprendidos en el Día 36
1. **Modelos de Respuesta (`response_model`):**
   * Filtrado automático de campos confidenciales o internos (como `salario`) antes de enviar la respuesta JSON al cliente.
   * Uso de tipos compuestos como `response_model=list[EmpleadoRespuesta]` para colecciones.
2. **Patrón DTO (Data Transfer Objects):**
   * Separación clara entre el modelo de entrada de datos (`EmpleadoCrear`) y el modelo público de salida (`EmpleadoRespuesta`).
   * Protección de la capa de transporte sin alterar la estructura de almacenamiento interno.

## 🛠️ Tecnologías y Herramientas utilizadas
* **Lenguaje:** Python 3
* **Framework:** FastAPI (`response_model`)
* **Validación:** Pydantic v2
* **Servidor ASGI:** Uvicorn
* **Control de Versiones:** Git & GitHub

---
_Proceso de aprendizaje guiado con auditorías de código diarias para asegurar la calidad del software._

## 💡 Conceptos Clave Aprendidos en el Día 37
1. **Método HTTP `PUT`:**
   * Utilizado para reemplazar/actualizar por completo un recurso existente en el servidor.
   * El identificador del recurso se envía en la URL (Path Parameter), permitiendo que el cuerpo de la petición (Request Body) solo contenga los datos a modificar.
2. **Arquitectura de DTOs Dinámica:**
   * Creación de esquemas específicos para cada operación (`EmpleadoCrear` con ID, `EmpleadoActualizar` sin ID).
   * Reutilización del esquema de salida `EmpleadoRespuesta` para mantener la privacidad de los datos sensibles de forma consistente en todos los endpoints.
3. **`PUT` vs `PATCH` (Estándares REST):**
   * **PUT:** Requiere enviar el objeto completo para reemplazar el existente.
   * **PATCH:** Se utiliza para aplicar modificaciones parciales (ej. cambiar solo un campo sin enviar el resto).

## 🛠️ Tecnologías y Herramientas utilizadas
* **Lenguaje:** Python 3
* **Framework:** FastAPI (`HTTPException`, `response_model`)
* **Validación:** Pydantic v2
* **Servidor ASGI:** Uvicorn
* **Control de Versiones:** Git & GitHub

---
_Proceso de aprendizaje guiado con auditorías de código diarias para asegurar la calidad del software._
