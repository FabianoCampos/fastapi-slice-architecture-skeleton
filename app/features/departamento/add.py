import uuid
from dataclasses import dataclass

from automapper import mapper
from mediatr import Mediator
from sqlmodel import select

from app.features.base_cqrs_handler import BaseCqrsHandler
from app.infrastructure.db.models.departamento import Departamento
from app.utils.exceptions.item_exists import ItemExistsException


@dataclass(frozen=True)
class AddDepartamentoCommand:
    nome: str
    local: str
    id_empresa: uuid


@Mediator.handler
class AddDepartamentoHandler(BaseCqrsHandler):
    def handle(self, request: AddDepartamentoCommand):
        self.itemExists(request.nome)
        identity = mapper.to(Departamento).map(request)

        self.db.add_all([identity])
        # self.db.commit()
        return identity

    def itemExists(self, nome: str):
        stmt = select(Departamento).where(Departamento.nome == nome)
        result = self.db.execute(stmt)
        total = len(result.scalars().all())
        if total > 0:
            raise ItemExistsException(
                f"Já existe um departamento com o nome '{nome}' cadastrado!"
            )
