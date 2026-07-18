from fastapi import FastAPI

# Instancia principal de la aplicacion 
app = FastAPI()

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

# ENDPOINT 3 - Tu primer recurso real 
@app.get("/empleado")
def obtener_empleado():
    """Retorna la lista de empleados del sistema."""
    return {
        "empleados": [
            {"id": 1, "nombre": "Carlos Perez", "cargo": "Backend Developer"},
            {"id": 2, "nombre": "Ana Gomez", "cargo": "QA Engineer"}
        ]
    }