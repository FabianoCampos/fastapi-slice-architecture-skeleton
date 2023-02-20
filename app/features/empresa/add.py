from dataclasses import dataclass

from automapper import mapper
from mediatr import Mediator
from sqlalchemy import select

from app.features.base_cqrs_handler import BaseCqrsHandler
from app.infrastructure.db.models.empresa import Empresa
from app.utils.exceptions.item_exists import ItemExistsException


@dataclass(frozen=True)
class AddEmpresaCommand:
    nome: str
    logradouro: str
    cidade: str
    estado: str
    matriz: bool


@Mediator.handler
class AddEmpresaHandler(BaseCqrsHandler):
    def handle(self, request: AddEmpresaCommand):
        self.itemExists(request.nome)
        identity = mapper.to(Empresa).map(request)

        self.db.add(identity)
        # self.db.commit() feito bia behavior
        return identity

    def itemExists(self, nome: str):
        stmt = select(Empresa).where(Empresa.nome == nome)
        result = self.db.execute(stmt)
        total = len(result.scalars().all())
        if total > 0:
            raise ItemExistsException(
                f"Já existe uma empresa com o nome '{nome}' cadastrado!"
            )
