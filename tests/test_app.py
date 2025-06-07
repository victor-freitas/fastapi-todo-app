from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_todo_app.app import app


def test_run():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}
