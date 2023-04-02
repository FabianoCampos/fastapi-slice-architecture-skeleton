import os
from typing import Generator

import pytest
from fastapi.testclient import TestClient

from app.core.config import settings
from app.infrastructure.db.migrations import run_sql_migrations
from app.main import app
from tests.fixtures.departamento import *
from tests.fixtures.empresa import *

settings.database_url = "sqlite+pysqlite:///./test.db"


def init_db_test():
    if os.path.exists("./test.db"):
        os.remove("./test.db")
    run_sql_migrations()


init_db_test()


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c
