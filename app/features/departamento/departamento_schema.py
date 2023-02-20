from pydantic import BaseModel, Field


class DepartamentoBase(BaseModel):
    nome: str = Field(default=None, title="Nome do departamento", max_length=250)
    local: str = Field(
        default=None, title="Local onde está localizado o departamento", max_length=250
    )
    id_empresa: str = Field(
        default=None,
        title="Id da empresa ao qual pertence o departamento",
        max_length=36,
    )


class Departamento(DepartamentoBase):
    id: str

    class Config:
        orm_mode = True


class DepartamentoAdd(DepartamentoBase):
    pass


class DepartamentoUpdate(DepartamentoBase):
    pass
