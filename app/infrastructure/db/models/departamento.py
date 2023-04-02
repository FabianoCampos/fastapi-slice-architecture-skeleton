import uuid
from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .empresa import Empresa


class Departamento(SQLModel, table=True):
    __tablename__ = "departamento"

    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )
    nome: str = Field(max_length=200, nullable=False)
    local: str = Field(max_length=200, nullable=False)
    id_empresa: uuid.UUID = Field(foreign_key="empresa.id")

    empresa: "Empresa" = Relationship(back_populates="departamentos")
