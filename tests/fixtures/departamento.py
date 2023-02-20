import pytest

from app.infrastructure.db.database import get_db
from app.infrastructure.db.models.departamento import Departamento
from app.infrastructure.db.models.empresa import Empresa


@pytest.fixture
def add_departamento_init_db_fixture(departamento_fixture, empresa_fixture):
    print("*****SETUP*****")
    db = get_db()
    db.query(Departamento).delete()
    db.query(Empresa).delete()
    db.commit()

    db.add_all(empresa_fixture)
    db.add_all(departamento_fixture)
    db.commit()
    yield db
    print("******TEARDOWN******")
    db.query(Departamento).delete()
    db.query(Empresa).delete()
    db.commit()
    db.close()


@pytest.fixture
def departamento_dict_add_fixture():
    return {
        "nome": "Analise Config",
        "local": "online",
        "id_empresa": "9e2b6d09-54be-46db-8007-82befa3aff9f",
    }


@pytest.fixture
def departamento_dict_fixture() -> list[dict]:
    return [
        {
            "id": "0ef7d170-14d9-4710-9470-80481f1145a9",
            "nome": "DevSecOps",
            "local": "online",
            "id_empresa": "9e2b6d09-54be-46db-8007-82befa3aff9f",
        },
        {
            "id": "8ab020e2-c5ed-4c8c-b883-affb72621e77",
            "nome": "EA - Arquitetura",
            "local": "online",
            "id_empresa": "9e2b6d09-54be-46db-8007-82befa3aff9f",
        },
        {
            "id": "a73d36a8-eb63-4a96-a349-7ec3163917ce",
            "nome": "SRE - Infra",
            "local": "online",
            "id_empresa": "9e2b6d09-54be-46db-8007-82befa3aff9f",
        },
    ]


@pytest.fixture
def departamento_fixture(departamento_dict_fixture) -> list[Departamento]:
    return [Departamento(**e) for e in departamento_dict_fixture]
