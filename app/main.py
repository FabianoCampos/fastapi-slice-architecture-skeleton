from contextlib import asynccontextmanager

from fastapi import FastAPI, logger
from starlette.middleware.base import BaseHTTPMiddleware

from app.core.config import settings
from app.infrastructure.db.migrations import run_sql_migrations
from app.middleware.db_middleware import init_session_instance
from app.routes import register_routes


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.logger.info("-- INICIANDO EXECUÇÂO ATUALIZAÇÂO DO BANCO DE DADOS --")
    run_sql_migrations()
    logger.logger.info("== FINALIZADA ATUALIZAÇÂO DO BANCO DE DADOS ==")
    yield


app = FastAPI(title=settings.app_name, version=settings.app_version, lifespan=lifespan)
app.add_middleware(BaseHTTPMiddleware, dispatch=init_session_instance)

register_routes(app)
