from unittest.mock import Mock

from fastapi.testclient import TestClient

from app.utils.exceptions.item_exists import ItemExistsException


def test_get_all_empresas_no_results(client: TestClient, mocker) -> None:
    fnmock = Mock()
    fnmock.return_value = []
    mocker.patch("mediatr.Mediator.send", fnmock)

    r = client.get("/api/empresa")
    assert 200 == r.status_code

    results = r.json()
    assert len(results) == 0


def test_get_all_empresas_with_results(
    client: TestClient, mocker, empresa_fixture
) -> None:
    fnmock = Mock()
    fnmock.return_value = empresa_fixture
    mocker.patch("mediatr.Mediator.send", fnmock)

    r = client.get("/api/empresa")
    assert 200 == r.status_code

    results = r.json()
    assert len(results) == len(empresa_fixture)


def test_add_empresa_ok(client: TestClient, mocker, empresa_dict_fixture) -> None:
    data = empresa_dict_fixture[0]

    fnmock = Mock()
    fnmock.return_value = data
    mocker.patch("mediatr.Mediator.send", fnmock)

    r = client.post(
        "/api/empresa",
        json=data,
    )
    assert 201 == r.status_code

    results = r.json()
    assert results["nome"] == data["nome"]


def test_add_empresa_conflict(client: TestClient, mocker, empresa_dict_fixture) -> None:
    fnmock = Mock(side_effect=ItemExistsException("conflito"))
    mocker.patch("mediatr.Mediator.send", fnmock)

    data = empresa_dict_fixture[0]
    r = client.post(
        "/api/empresa",
        json=data,
    )
    assert 409 == r.status_code


def test_add_empresa_error(client: TestClient, mocker, empresa_dict_fixture) -> None:
    fnmock = Mock(side_effect=Exception("error 500"))
    mocker.patch("mediatr.Mediator.send", fnmock)

    data = empresa_dict_fixture[0]
    r = client.post(
        "/api/empresa",
        json=data,
    )
    assert 500 == r.status_code
