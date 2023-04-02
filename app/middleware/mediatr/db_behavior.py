from mediatr import Mediator

from app.core.logging import logger
from app.infrastructure.db.database import DatabaseContext


@Mediator.behavior
def db_behavior(request: object, next):  # behavior atende a todas as requisições
    logger.debug("Dentro do db_behavior")
    result = next()
    logger.debug("Confirmando todas as alterações caso existam")
    DatabaseContext.commit()
    logger.debug("Retornando resultado")
    return result
