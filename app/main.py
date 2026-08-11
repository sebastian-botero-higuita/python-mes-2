# app/main.py
from app.routers import empleados
from fastapi import FastAPI

app = FastAPI(
    title="API de Gestión de Empleados (Modular)",
    description="API REST modularizada con separación de capas (Schemas, Database, Routers)",
    version="2.0.0",
)

# Registramos el router de empleados en la aplicación principal
app.include_router(empleados.router)


@app.get("/")
def leer_raiz():
    return {
        "mensaje": "¡Servidor FastAPI Modular funcionando correctamente!",
        "estado": "activo",
    }


@app.get("/salud")
def verificar_salud():
    return {"estado": "activo", "servidor": "FastAPI Modular"}