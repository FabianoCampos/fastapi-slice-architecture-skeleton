from unittest.mock import Mock

from fastapi.testclient import TestClient
from app.features.healthcheck.health_controller import is_database_online

from app.features.healthcheck.health_schemas import StatusHealth
from sqlalchemy.exc import SQLAlchemyError

def test_health_status_healthy(client: TestClient, mocker) -> None:
    fnmock = Mock()
    fnmock.return_value = True
    mocker.patch(
        "app.features.healthcheck.health_controller.is_database_online", fnmock
    )

    r = client.get("/health")
    assert 200 == r.status_code

    results = r.json()
    assert results["status"] == StatusHealth.HEALTHY
    assert results["entities"]["database"] == StatusHealth.HEALTHY


def test_health_status_unhealthy(client: TestClient, mocker) -> None:
    fnmock = Mock()
    fnmock.return_value = False
    mocker.patch(
        "app.features.healthcheck.health_controller.is_database_online", fnmock
    )

    r = client.get("/health")
    assert 503 == r.status_code

    results = r.json()
    assert results["status"] == StatusHealth.UNHEALTHY
    assert results["entities"]["database"] == StatusHealth.UNHEALTHY


def test_database_online_ok(mocker):
    fnmock = Mock()
    mocker.patch("app.infrastructure.db.database.get_db", Mock())
    mocker.patch("sqlalchemy.orm.Session.execute", Mock())
    result = is_database_online()
    assert result == True

def test_database_online_fail(mocker):
    mocker.patch("app.infrastructure.db.database.get_db", Mock())
    fnmock = Mock(side_effect=SQLAlchemyError("conflito"))
    mocker.patch("sqlalchemy.orm.Session.execute", fnmock)
    result = is_database_online()
    assert result == False
