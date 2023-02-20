import uuid
from dataclasses import dataclass

from mediatr import Mediator

from app.features.base_cqrs_handler import BaseCqrsHandler
from app.infrastructure.db.models.departamento import Departamento


@dataclass(frozen=True)
class GetAllDepartamentosQuery:
    id_empresa: uuid
    skip: int = 0
    limit: int = 100
    pass


@Mediator.handler
class GetAllDepartamentosHandler(BaseCqrsHandler):
    def handle(self, request: GetAllDepartamentosQuery):
        return (
            self.db.query(Departamento)
            .where(Departamento.id_empresa == str(request.id_empresa))
            .offset(request.skip)
            .limit(request.limit)
            .all()
        )
