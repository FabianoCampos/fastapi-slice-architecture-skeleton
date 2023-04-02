import uuid
from typing import Optional

from sqlmodel import Field, SQLModel


class Pessoa(SQLModel, table=True):
    __tablename__ = "pessoa"

    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )
    nome: str = Field(max_length=200, nullable=False)
    email: Optional[str] = Field(max_length=250)
    telefone: Optional[str] = Field(max_length=20)
