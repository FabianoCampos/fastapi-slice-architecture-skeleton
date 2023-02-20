import uuid
from typing import List

from automapper import mapper
from fastapi import APIRouter, HTTPException

from app.core.logging import logger
from app.core.mediator import mediator
from app.utils.exceptions.item_exists import ItemExistsException

from .add import AddDepartamentoCommand
from .departamento_schema import Departamento, DepartamentoAdd
from .get_all import GetAllDepartamentosQuery

router = APIRouter(
    prefix="/api/departamento",
    tags=["departamento"],
    responses={404: {"description": "Not found"}},
)


@router.get(
    "/{id_empresa}",
    response_model=List[Departamento],
    name="Lista de departamentos por empresa",
)
def get_all(id_empresa: str, skip: int | None = 0, limit: int | None = 100):
    logger.debug("Buscando os departamento da empresa...")
    result = mediator.send(
        GetAllDepartamentosQuery(
            limit=limit, skip=skip, id_empresa=uuid.UUID(id_empresa)
        )
    )
    logger.debug("Retornando resultado...")
    return result


@router.post(
    "",
    response_model=Departamento,
    name="Adiciona departamento em uma empresa",
    status_code=201,
    responses={409: {"detail": "Registro existente"}},
)
def add(form: DepartamentoAdd):
    logger.debug("Inserindo registro no banco de dados...")
    try:
        command = mapper.to(AddDepartamentoCommand).map(form)
        result = mediator.send(command)
        return result
    except ItemExistsException as ex:
        msg = f"Erro ao inserir registro: {ex}"
        logger.error(msg)
        raise HTTPException(
            status_code=409,
            detail=msg,
        )
    except Exception as ex:
        msg = f"Erro ao inserir registro: {ex}"
        logger.error(msg)
        raise HTTPException(
            status_code=500,
            detail=msg,
        )
