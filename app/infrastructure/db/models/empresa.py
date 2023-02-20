import uuid
from typing import Any

from sqlalchemy import Boolean, Column, String
from sqlalchemy.orm import relationship

from app.infrastructure.db.database import Base


class Empresa(Base):
    __tablename__ = "empresa"

    id = Column(String(36), primary_key=True, index=True)
    nome = Column(String(250), nullable=False)
    logradouro = Column(String(250))
    cidade = Column(String(150), default=True)
    estado = Column(String(50), default=True)
    matriz = Column(Boolean, default=True)

    departamentos = relationship("Departamento", back_populates="empresa")

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        self.id = str(uuid.uuid4())
        super().__init__(*args, **kwargs)
