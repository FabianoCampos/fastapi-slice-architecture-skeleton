from app.features.empresa.get_all import GetAllEmpresasHandler, GetAllEmpresasQuery


def test_get_all_empresas_paginado(add_empresa_init_db_fixture) -> None:
    query = GetAllEmpresasHandler()
    result = query.handle(GetAllEmpresasQuery(skip=0, limit=1))
    assert len(result) == 1


def test_get_all_empresas(add_empresa_init_db_fixture, empresa_fixture) -> None:
    query = GetAllEmpresasHandler()
    result = query.handle(GetAllEmpresasQuery(skip=0, limit=10000))
    assert len(result) == len(empresa_fixture)
