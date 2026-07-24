from fastapi import FastAPI

# Instancia principal de la aplicacion 
app = FastAPI()

# Base de datos simulada en memoria 
EMPLEADOS = [
    {"id": 1, "nombre": "Carlos Perez", "cargo": "Backen Developer"},
    {"id": 2, "nombre": "Ana Gomez", "cargo": "QA Engineer"},
    {"id": 3, "nombre": "Sebastian Botero", "cargo": "Backend Developer"},
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

# 3 Query Parameter: Obtener todos o filtrar por cargo (?cargo=Backend)
@app.get("/empleados")
def obtener_empleados(cargo: str | None = None):
    """Si el cliente pasa _?cargo=..., filtramos. si no, devolvemos todos"""
    if cargo:
        filtrados = [emp for emp in EMPLEADOS if emp["cargo"].lower() == cargo.lower()]
        return {"total": len(filtrados), "empleados": filtrados}
    return {"total": len(EMPLEADOS), "empleados": EMPLEADOS}

#4 Path Parameter: Obtener un empleado por su ID (/empleados/1)
@app.get("/empleados/{empleado_id}")
def obtener_empleado_por_id(empleado_id: int):
    """FastAPI valida automaticamente que 'empleado_id' sea un entero (int)."""
    for emp in EMPLEADOS:
        if emp["id"] == empleado_id:
            return {"empleado": emp}
    return {"error": f"Empleado con ID {empleado_id} no fue encontrado"}

