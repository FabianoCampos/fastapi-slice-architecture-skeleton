import uuid
from typing import Any

from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.infrastructure.db.database import Base


class Departamento(Base):
    __tablename__ = "departamento"

    id = Column(String(36), primary_key=True, index=True)
    nome = Column(String(200), nullable=False)
    local = Column(String(200), nullable=False)
    id_empresa = Column(String(36), ForeignKey("empresa.id"))

    empresa = relationship("Empresa", back_populates="departamentos")

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        self.id = str(uuid.uuid4())
        super().__init__(*args, **kwargs)
