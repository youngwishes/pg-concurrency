from pathlib import Path
from os import getenv

from pydantic import Field
from pydantic_settings import BaseSettings

import logging.config
import os

from core.enums import IsolationEnum, PostgresInterfaceEnum


class Settings(BaseSettings):
    ROOT_DIR: Path = Path(__name__).absolute().parent.joinpath("src")
    TEMPLATES_ROOT: Path = ROOT_DIR.joinpath("templates")

    DEFAULT_ISOLATION_LEVEL: IsolationEnum = Field(
        IsolationEnum.READ_COMMITTED, description="Уровень изоляций по умолчанию"
    )
    DEFAULT_IS_SCHEMA_CREATED: bool = Field(
        False, description="Создана ли схема по умолчанию при первом запуске"
    )
    DEFAULT_IS_DB_POPULATED: bool = Field(
        False, description="Наполнена ли БД данными по умолчанию при первом запуске"
    )
    POOLS_COUNT: int = Field(
        2,
        description="Количество одновременных подключений к базе (проект настроен на 2)",
        frozen=True,
    )
    MIN_SIZE: int = 10
    MAX_SIZE: int = 100

    @staticmethod
    def resolve_postgres_uri(interface: PostgresInterfaceEnum) -> str:
        if interface == PostgresInterfaceEnum.ASYNCPG:
            driver = "postgres"
        else:
            driver = "postgresql+asyncpg"

        return "{driver}://{username}:{password}@{host}:{port}/{db_name}".format(
            driver=driver,
            username=getenv("POSTGRES_USERNAME", default="postgres"),
            password=getenv("POSTGRES_PASSWORD", default="postgres"),
            host=getenv("POSTGRES_HOST", default="localhost"),
            port=getenv("POSTGRES_PORT", default=5432),
            db_name=getenv("POSTGRES_DB", default="postgres"),
        )


settings = Settings()


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "app": {
            "format": "[%(asctime)s] %(message)s",
            "datefmt": "%H:%M:%S",
        },
    },
    "handlers": {
        "app": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": os.path.join(settings.ROOT_DIR, "concurrency.log"),
            "formatter": "app",
        },
    },
    "loggers": {
        "concurrency": {
            "handlers": ["app"],
            "level": "DEBUG",
            "propagate": True,
        },
    },
}

logging.config.dictConfig(LOGGING)
