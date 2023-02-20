from unittest.mock import Mock

from fastapi.testclient import TestClient

from app.utils.exceptions.item_exists import ItemExistsException

id_empresa = "9e2b6d09-54be-46db-8007-82befa3aff9f"


def test_get_all_departamentos_no_results(client: TestClient, mocker) -> None:
    fnmock = Mock()
    fnmock.return_value = []
    mocker.patch("mediatr.Mediator.send", fnmock)

    r = client.get(f"/api/departamento/{id_empresa}")
    assert 200 == r.status_code

    results = r.json()
    assert len(results) == 0


def test_get_all_departamentos_with_results(
    client: TestClient, mocker, departamento_fixture
) -> None:
    data = list(filter(lambda x: (x.id_empresa == id_empresa), departamento_fixture))
    fnmock = Mock()
    fnmock.return_value = data
    mocker.patch("mediatr.Mediator.send", fnmock)

    r = client.get(f"/api/departamento/{id_empresa}")
    assert 200 == r.status_code

    results = r.json()
    assert len(results) == len(data)


def test_add_departamento_ok(
    client: TestClient, mocker, departamento_dict_fixture
) -> None:
    data = departamento_dict_fixture[0]

    fnmock = Mock()
    fnmock.return_value = data
    mocker.patch("mediatr.Mediator.send", fnmock)

    r = client.post(
        "/api/departamento",
        json=data,
    )
    assert 201 == r.status_code

    results = r.json()
    assert results["nome"] == data["nome"]


def test_add_departamento_conflict(
    client: TestClient, mocker, departamento_dict_fixture
) -> None:
    fnmock = Mock(side_effect=ItemExistsException("conflito"))
    mocker.patch("mediatr.Mediator.send", fnmock)

    data = departamento_dict_fixture[0]
    r = client.post(
        "/api/departamento",
        json=data,
    )
    assert 409 == r.status_code


def test_add_departamento_error(
    client: TestClient, mocker, departamento_dict_fixture
) -> None:
    fnmock = Mock(side_effect=Exception("error 500"))
    mocker.patch("mediatr.Mediator.send", fnmock)

    data = departamento_dict_fixture[0]
    r = client.post(
        "/api/departamento",
        json=data,
    )
    assert 500 == r.status_code
