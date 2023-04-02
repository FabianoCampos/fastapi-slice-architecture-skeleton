import uuid

from pydantic import BaseModel, Field


class EmpresaBase(BaseModel):
    nome: str
    logradouro: str = Field(
        default=None, title="Endereço da cidade da empresa", max_length=250
    )
    cidade: str = Field(default=None, title="Cidade da empresa", max_length=250)
    estado: str = Field(
        default=None, title="Estado onde está localizada a empresa", max_length=250
    )
    matriz: bool = Field(default=False, title="Informe se a empresa é a matriz")


class Empresa(EmpresaBase):
    id: uuid.UUID

    class Config:
        orm_mode = True


class EmpresaAdd(EmpresaBase):
    pass


class EmpresaUpdate(EmpresaBase):
    pass
