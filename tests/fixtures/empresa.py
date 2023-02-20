import pytest

from app.infrastructure.db.database import get_db
from app.infrastructure.db.models.empresa import Empresa


@pytest.fixture
def add_empresa_init_db_fixture(empresa_fixture):
    print("*****SETUP*****")
    db = get_db()
    db.query(Empresa).delete()
    db.commit()

    db.add_all(empresa_fixture)
    db.commit()
    yield db
    print("******TEARDOWN******")
    db.query(Empresa).delete()
    db.commit()
    db.close()


@pytest.fixture
def empresa_dict_add_fixture():
    return {
        "nome": "Empresa Alpha",
        "logradouro": "Rua Empresa Alpha",
        "cidade": "SP",
        "estado": "SP",
        "matriz": True,
    }


@pytest.fixture
def empresa_dict_fixture() -> list[dict]:
    return [
        {
            "id": "9e2b6d09-54be-46db-8007-82befa3aff9f",
            "nome": "Empresa A",
            "logradouro": "Rua Empresa A",
            "cidade": "SP",
            "estado": "SP",
            "matriz": True,
        },
        {
            "id": "15598528-e683-4d65-9242-f6331da7be4d",
            "nome": "Empresa B",
            "logradouro": "Rua Empresa B",
            "cidade": "Florianópolis",
            "estado": "SC",
            "matriz": False,
        },
        {
            "id": "2c734b17-6cb7-475f-919b-50a1464a31c1",
            "nome": "Empresa C",
            "logradouro": "Rua Empresa C",
            "cidade": "Belo Horizonte",
            "estado": "MG",
            "matriz": False,
        },
    ]


@pytest.fixture
def empresa_fixture(empresa_dict_fixture) -> list[Empresa]:
    return [Empresa(**e) for e in empresa_dict_fixture]
