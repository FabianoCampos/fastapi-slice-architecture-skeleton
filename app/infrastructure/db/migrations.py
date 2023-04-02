import os

from alembic.command import upgrade
from alembic.config import Config
from app.core.config import settings


def run_sql_migrations():
    """
    Executa as migrações SQL no banco de dados usando Alembic.

    Esta função usa a biblioteca Alembic para atualizar o banco de dados para a última
    revisão disponível. O caminho para o diretório raiz de migração é definido como
    "alembic/" no diretório de trabalho atual. O arquivo de configuração "alembic.ini"
    é procurado um nível acima do diretório de migração. A URL do banco de dados é
    lida da variável de ambiente "DATABASE_URL" definida no arquivo ".env".

    Args:
        None

    Returns:
        None
    """
    migrations_dir = os.path.join(os.getcwd(), "alembic")
    config_file = os.path.join(migrations_dir, "..", "alembic.ini")

    config = Config(file_=config_file)
    config.set_main_option("script_location", migrations_dir)
    config.set_main_option("sqlalchemy.url", settings.database_url)
    config.set_section_option("logger_alembic", "level", settings.logging_level.upper())
    config.set_section_option(
        "logger_sqlalchemy", "level", settings.logging_level.upper()
    )
    config.set_section_option("logger_fastapi", "level", settings.logging_level.upper())
    config.attributes["configure_logger"] = False

    # upgrade the database to the latest revision
    upgrade(config, "head")
