from app.features.departamento.get_all import (
    GetAllDepartamentosHandler,
    GetAllDepartamentosQuery,
)

id_empresa = "9e2b6d09-54be-46db-8007-82befa3aff9f"


def test_get_all_departamentos_paginado(add_departamento_init_db_fixture) -> None:
    query = GetAllDepartamentosHandler()
    result = query.handle(
        GetAllDepartamentosQuery(id_empresa=id_empresa, skip=0, limit=1)
    )
    assert len(result) == 1


def test_get_all_departamentos(
    add_departamento_init_db_fixture, departamento_fixture
) -> None:
    query = GetAllDepartamentosHandler()
    result = query.handle(
        GetAllDepartamentosQuery(id_empresa=id_empresa, skip=0, limit=10000)
    )
    assert len(result) == len(departamento_fixture)
