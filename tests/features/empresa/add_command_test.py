import pytest

from app.features.empresa.add import AddEmpresaCommand, AddEmpresaHandler
from app.utils.exceptions.item_exists import ItemExistsException


def test_command_add_empresas_ok(empresa_dict_add_fixture) -> None:
    command = AddEmpresaHandler()
    result = command.handle(AddEmpresaCommand(**empresa_dict_add_fixture))
    assert result.nome == empresa_dict_add_fixture["nome"]


def test_command_add_empresas_conflict(
    add_empresa_init_db_fixture, empresa_dict_fixture
) -> None:
    query = AddEmpresaHandler()
    data = empresa_dict_fixture[0]
    del data["id"]
    with pytest.raises(ItemExistsException):
        query.handle(AddEmpresaCommand(**data))
