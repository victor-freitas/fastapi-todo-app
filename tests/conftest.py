import pytest
from fastapi.testclient import TestClient

from fastapi_todo_app.app import app


@pytest.fixture
def client():
    return TestClient(app)
