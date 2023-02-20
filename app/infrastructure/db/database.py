from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker

from app.core.config import settings

Base = declarative_base()


class DatabaseContext:
    db: Session = None
    SessionLocal: sessionmaker[Session] = None

    @staticmethod
    def init_db():
        engine = create_engine(settings.database_url, pool_pre_ping=True)
        DatabaseContext.SessionLocal = sessionmaker(
            autocommit=False, autoflush=False, bind=engine
        )

    @staticmethod
    def get_db() -> Session:
        if (
            not DatabaseContext.SessionLocal
            or isinstance(DatabaseContext.db, Session) is False
        ):
            DatabaseContext.init_db()
            DatabaseContext.db = DatabaseContext.SessionLocal()

        return DatabaseContext.db

    @staticmethod
    def close_conn():
        if DatabaseContext.db:
            DatabaseContext.db.close_all()

    @staticmethod
    def commit():
        db = DatabaseContext.db
        if db and db.new or db.deleted or db.dirty:
            DatabaseContext.db.commit()


def get_db():
    return DatabaseContext.get_db()
