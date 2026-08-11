# app/schemas.py
from pydantic import BaseModel


# 1. Esquema de Entrada para Creación
class EmpleadoCrear(BaseModel):
    id: int
    nombre: str
    cargo: str
    salario: float


# 2. Esquema de Entrada para Actualización
class EmpleadoActualizar(BaseModel):
    nombre: str
    cargo: str
    salario: float


# 3. Esquema de Salida Pública (DTO de Respuesta)
class EmpleadoRespuesta(BaseModel):
    id: int
    nombre: str
    cargo: str

    