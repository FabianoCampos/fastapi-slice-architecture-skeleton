import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "FastApi Skeleton for Vertical Slice Architecture"
    database_url: str
    app_version: str = "local_develop"
    logging_level: str = "info"
    vault_endpoint: str = ""
    vault_k8s_role: str = ""
    vault_mount_point: str = ""

    class Config:
        env_file = os.path.join(os.getcwd(), "app", ".env")


settings = Settings()
