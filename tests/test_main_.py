# tests/test_main.py
from app.main import app
from fastapi.testclient import TestClient

# Instanciamos el cliente de pruebas conectado a nuestra aplicacion FastAPI
client = TestClient(app)

def test_leer_raiz_exitoso():
    #Realizamos una peticion GET simulada a la raiz '/'
    response = client.get("/")

    # 1. Verificamos que el codigo de estado sea 200 OK
    assert response.status_code == 200

    # 2. Verificamos que la estructura del JSON sea exacta
    assert response.json() == {"mensaje": "¡Servidor FastAPI Modular funcionando correctamente!",
                               "estado": "activo",
    }
def test_verificar_salud_exitoso():
    response = client.get("/salud")

    assert response.status_code == 200
    datos = response.json()
    assert datos["estado"] == "activo"
    assert datos["servidor"] == "FastAPI Modular"

