import os
from typing import Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine

from app.core.config import settings
from app.infrastructure.db.database import Base
from app.main import app
from tests.fixtures.departamento import *
from tests.fixtures.empresa import *

settings.database_url = "sqlite+pysqlite:///./test.db"


def init_db_test():
    engine = create_engine(
        settings.database_url,
        echo=True,
        future=True,
        connect_args={"check_same_thread": False},
    )

    Base.metadata.create_all(bind=engine)


if os.path.exists("./test.db"):
    os.remove("./test.db")


init_db_test()


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c
