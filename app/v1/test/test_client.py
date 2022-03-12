from fastapi.testclient import TestClient
from main import app

def test_create_client_ok():
    client = TestClient(app)

    cliente = {
        'nombre': 'cliente_test',
        "email": "cliente@gmail.com",
    }

    response = client.get(
        '/api/v1/client',
        data=cliente,
    )
    assert response.status_code == 201, response.text
    # assert data['nombre'] == cliente['nombre']def test_create_client_ok():


def test_list_client_ok():
    client = TestClient(app)


    response = client.get(
        '/api/v1/client',
    )
    assert response.status_code == 200, response.text
    # assert data['nombre'] == cliente['nombre']