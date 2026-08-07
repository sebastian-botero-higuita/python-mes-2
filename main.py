from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

# Instancia principal de la aplicacion 
app = FastAPI()

# 1. Definimos el esquema de datos con Pydantic (Escudo Protector)
# 2. Esquema de Entrada (Incluye datos sensibles/privados)
class EmpleadoCrear(BaseModel):
    id: int
    nombre: str
    cargo: str
    salario: float # Dato privado que NO debe exponerse en la salida 

class EmpleadoActualizar(BaseModel):
    nombre: str 
    cargo: str
    salario: float

# 3. Esquema de Salida (Filtro publico de respuesta)
class EmpleadoRespuesta(BaseModel):
    id: int
    nombre: str
    cargo: str

# Base de datos simulada en memoria 
EMPLEADOS = [
    {"id": 1, "nombre": "Carlos Perez", "cargo": "Backend Developer", "salario": 3500.0},
    {"id": 2, "nombre": "Ana Gomez", "cargo": "QA Engineer", "salario": 3000.0},
    {"id": 3, "nombre": "Sebastian Botero", "cargo": "Backend Developer", "salario": 4000.0},
]


# ENDPOINT 1 - Raiz del servidor
@app.get("/")
def leer_raiz():
    """ Endpoint de bienvenida, Verifica que el servidor esta vivo."""
    return {"mensaje": " Servidor FastAPI funcionando !", "version": "1.0"}

# ENDPOINT 2 - Health check
@app.get("/salud")
def verificar_salud():
    """Health check: confirmar que el servidor responde correctamente."""
    return {"estado": "activo", "servidor": "FastAPI"}

# Aplicamos response model en dorma de lista para filtrar la salida del GET
# 3 Query Parameter: Obtener todos o filtrar por cargo (?cargo=Backend)
@app.get("/empleados", response_model=list[EmpleadoRespuesta])
def obtener_empleados(cargo: str | None = None):
    if cargo:
        return [emp for emp in EMPLEADOS if emp["cargo"].lower() == cargo.lower()]
    return EMPLEADOS

#4 Manejo sematico de Errores: HTTP 404 Not Found
# Aplicamos response_model para filtrar la salida de un solo objeto por ID
@app.get("/empleados/{empleado_id}", response_model=EmpleadoRespuesta)
def obtener_empleado_por_id(empleado_id: int):
    """FastAPI valida automaticamente que 'empleado_id' sea un entero (int)."""
    for emp in EMPLEADOS:
        if emp["id"] == empleado_id:
            return  emp

    # Lanzamos una excepcion HTTP nativa de FastAPI
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Empleado con ID {empleado_id} no fue encontrado",
    )

# Respuestas HTTP Sematica: 201 Created al crear un recurso 
# 5. Metodo POST: Crear un nuevo empleado recibiendo datos en el Request Body
# Aplicamos response_model en el POST

@app.post("/empleados", status_code=status.HTTP_201_CREATED, response_model=EmpleadoRespuesta)
def crear_empleado(nuevo_empleado: EmpleadoCrear):
    empleado_dict = nuevo_empleado.model_dump()
    EMPLEADOS.append(empleado_dict)

 # Retomamos el diccionario completo (que SI tiene salario),
 # pero FastAPI lo filtrara usando EmpleadoRespuesta.
    return empleado_dict

# Actualizacion completa de un recurso mediante el metodo PUT
@app.put("/empleados/{empleado_id}", response_model=EmpleadoRespuesta)
def actualizar_empleado(empleado_id: int, datos_actualizados: EmpleadoActualizar):

    """Recibe un ID por URL y los nuevos datos en el Body.
        Si el empleado exist, actualiza sus campos y retorna el objeto filtrado por response_model."""

    for emp in EMPLEADOS:
      if emp["id"] == empleado_id:
        datos_dict = datos_actualizados.model_dump()
        emp["nombre"] = datos_dict["nombre"]
        emp["cargo"] = datos_dict["cargo"]
        emp["salario"] = datos_dict["salario"]
        return emp

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"No se puede actualizar. Empleado con ID {empleado_id} no fue encontrado",
)

# Eliminacion de recursos mediante el metodo DELETE
@app.delete("/empleados/{empleado_id}")
def eliminar_empleado(empleado_id: int):
    """Busca un empleado por ID en la lista.
        si existe, lo remueve mediante pop() y retorna una confirmacion.
        si no existe, lanza una excepcion HTTP 404."""
    for index, emp in enumerate(EMPLEADOS):
        if emp["id"] == empleado_id:
            empleado_eliminado = EMPLEADOS.pop(index)
            return { "mensaje": f"Empleado con ID {empleado_id} eliminado con exito",
                   "empleado_eliminado": empleado_eliminado["nombre"],
            }
    raise HTTPException(
         status_code=status.HTTP_404_NOT_FOUND,
         detail=f"No se puede eliminar. Empleado con ID {empleado_id} no fue encontrado"
     )