import pytest

from app.features.departamento.add import AddDepartamentoCommand, AddDepartamentoHandler
from app.utils.exceptions.item_exists import ItemExistsException


def test_command_add_departamentos_ok(departamento_dict_add_fixture) -> None:
    command = AddDepartamentoHandler()
    result = command.handle(AddDepartamentoCommand(**departamento_dict_add_fixture))
    assert result.nome == departamento_dict_add_fixture["nome"]


def test_command_add_departamentos_conflict(
    add_departamento_init_db_fixture, departamento_dict_fixture
) -> None:
    query = AddDepartamentoHandler()
    data = departamento_dict_fixture[0]
    del data["id"]
    with pytest.raises(ItemExistsException):
        query.handle(AddDepartamentoCommand(**data))
