from fastapi.testclient import TestClient
from main import app

def test_cuenta_ok():
    client = TestClient(app)


    response = client.get(
        '/api/v1/cuenta/1',
    )
    assert response.status_code == 200, response.text
    # assert data['nombre'] == cliente['nombre']