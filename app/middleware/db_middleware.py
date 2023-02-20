from fastapi import Request

from app.core.logging import logger
from app.infrastructure.db.database import DatabaseContext


async def init_session_instance(request: Request, call_next):
    response = await call_next(request)

    logger.info("Fechando as conexoes com o banco abertas")
    DatabaseContext.close_conn()
    return response
