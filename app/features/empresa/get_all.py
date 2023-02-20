from dataclasses import dataclass

from mediatr import Mediator
from sqlalchemy import desc, select

from app.features.base_cqrs_handler import BaseCqrsHandler
from app.infrastructure.db.models.empresa import Empresa


@dataclass(frozen=True)
class GetAllEmpresasQuery:
    skip: int = 0
    limit: int = 100
    pass


@Mediator.handler
class GetAllEmpresasHandler(BaseCqrsHandler):
    def handle(self, request: GetAllEmpresasQuery):
        stmt = (
            select(Empresa)
            .order_by(desc(Empresa.nome))
            .offset(request.skip)
            .limit(request.limit)
        )
        # print(stmt)
        result = self.db.execute(stmt)
        return result.scalars().all()
