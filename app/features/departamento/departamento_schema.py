import uuid

from pydantic import BaseModel, Field


class DepartamentoBase(BaseModel):
    nome: str = Field(default=None, title="Nome do departamento", max_length=250)
    local: str = Field(
        default=None, title="Local onde está localizado o departamento", max_length=250
    )
    id_empresa: uuid.UUID = Field(
        default=None, title="Id da empresa ao qual pertence o departamento"
    )


class Departamento(DepartamentoBase):
    id: uuid.UUID

    class Config:
        orm_mode = True


class DepartamentoAdd(DepartamentoBase):
    pass


class DepartamentoUpdate(DepartamentoBase):
    pass
