from sqlmodel import Session, create_engine

from app.core.config import settings


class DatabaseContext:
    __db: Session = None

    @staticmethod
    def __init_db():
        engine = create_engine(settings.database_url, pool_pre_ping=True)
        DatabaseContext.__db = Session(engine)

    @staticmethod
    def get_db() -> Session:
        if isinstance(DatabaseContext.__db, Session) is False:
            DatabaseContext.__init_db()

        return DatabaseContext.__db

    @staticmethod
    def close_conn():
        if DatabaseContext.__db:
            DatabaseContext.__db.close_all()

    @staticmethod
    def commit():
        db = DatabaseContext.__db
        if db and db.new or db.deleted or db.dirty:
            DatabaseContext.__db.commit()


def get_db():
    return DatabaseContext.get_db()
