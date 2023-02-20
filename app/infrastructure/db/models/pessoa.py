import uuid
from typing import Any

from sqlalchemy import Column, String

from app.infrastructure.db.database import Base


class Pessoa(Base):
    __tablename__ = "pessoa"

    id = Column(String(36), primary_key=True, index=True)
    nome = Column(String(200), nullable=False)
    email = Column(String(250))
    telefone = Column(String(20))

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        self.id = str(uuid.uuid4())
        super().__init__(*args, **kwargs)
