from typing import List

from automapper import mapper
from fastapi import APIRouter, HTTPException

from app.core.logging import logger
from app.core.mediator import mediator
from app.utils.exceptions.item_exists import ItemExistsException

from .add import AddEmpresaCommand
from .empresa_schema import Empresa, EmpresaAdd
from .get_all import GetAllEmpresasQuery

router = APIRouter(
    prefix="/api/empresa",
    tags=["empresa"],
    responses={404: {"description": "Not found"}},
)


@router.get("", response_model=List[Empresa], name="ListEmpresa")
def get_all(skip: int | None = 0, limit: int | None = 100):
    logger.debug("Buscando as empresas...")
    result = mediator.send(GetAllEmpresasQuery(limit=limit, skip=skip))
    logger.debug("Retornando resultado...")
    return result


@router.post(
    "",
    response_model=Empresa,
    name="AddEmpresa",
    status_code=201,
    responses={409: {"detail": "Registro existente"}},
)
def add(form: EmpresaAdd):
    logger.debug("Inserindo registro no banco de dados...")
    try:
        command = mapper.to(AddEmpresaCommand).map(form)
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
