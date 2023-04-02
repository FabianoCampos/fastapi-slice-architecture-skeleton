import uuid
from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel

from app.infrastructure.db.models.departamento import Departamento


class Empresa(SQLModel, table=True):
    __tablename__ = "empresa"

    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )
    nome: str = Field(max_length=250, nullable=False)
    logradouro: Optional[str] = Field(max_length=250)
    cidade: Optional[str] = Field(max_length=150)
    estado: Optional[str] = Field(max_length=50)
    matriz: bool = Field(nullable=False)

    departamentos: List["Departamento"] = Relationship(back_populates="empresa")
