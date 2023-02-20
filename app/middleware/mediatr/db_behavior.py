from mediatr import Mediator

from app.core.logging import logger
from app.infrastructure.db.database import DatabaseContext


@Mediator.behavior
def db_behavior(
    request: object, next
):  # behavior atende a todas as requisições
    logger.info("Dentro do db_behavior")
    result = next()
    logger.info("Confirmando todas as alterações caso existam")
    DatabaseContext.commit()
    logger.info("Retornando resultado")
    return result
