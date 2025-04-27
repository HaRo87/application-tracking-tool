import pytest

from http import HTTPStatus

from fastapi.testclient import TestClient

from src.foundation.common import META_DATA
from src.main import app


@pytest.mark.system
def test_v1_get_meta_data_returns_correct_data():
    response = TestClient(app).get("/v1/meta")
    assert response.status_code == HTTPStatus.OK
    assert response.json()["version"] == META_DATA.version
