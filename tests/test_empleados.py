# tests/test_empleados.py
from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

# 1. Prueba de listado general 
def test_obtener_empleados_lista():
    response = client.get("/empleados")

    assert response.status_code == 200 
    datos = response.json()
    assert isinstance(datos, list)
    assert len(datos) >= 3

# 2. Prueba de busqueda por ID exitosa y verificacion de DTO
def test_obtener_empleado_por_id_exitoso():
    response = client.get("/empleados/1")

    assert response.status_code == 200 
    datos = response.json()
    assert datos["id"] == 1
    assert datos["nombre"] == "Carlos Pérez"

    # VALIDACION DE SEGURIDAD (DTO): El salario NO debe ser expuesto
    assert "salario" not in datos

# 3. Prueba de error 404 para ID inexistente
def test_obtener_empleado_por_id_no_encontrado():
    response = client.get("/empleados/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Empleado con ID 999 no fue encontrado" 

# 4. Prueba de creacion de un nuevo empleado
def test_crear_empleado_exitoso():
    nuevo_empleado = {
        "id": 10,
        "nombre": "Laura Restrepo",
        "cargo": "DevOps Engineer",
        "salario": 4500.0
    }
    response = client.post("/empleados", json=nuevo_empleado)

    assert response.status_code == 201
    datos = response.json()
    assert datos["id"] == 10
    assert datos["nombre"] == "Laura Restrepo"

    # Confirmamos nuevamente que el DTO filtra el salario en la respuesta
    assert "salario" not in datos
