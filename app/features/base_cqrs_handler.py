from sqlalchemy.orm import Session

from app.infrastructure.db.database import get_db


class BaseCqrsHandler:
    db: Session

    def __init__(self) -> None:
        self.db = get_db()

    # def __del__(self):
    #     self.db.close()
