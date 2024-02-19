from fastapi.testclient import TestClient

from helloworld import main


def test_main():
    client = TestClient(main.app)
    response = client.get("/")
    assert response.json() == {"message": "Hello World"}
