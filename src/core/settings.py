from pathlib import Path
from os import getenv
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ROOT_DIR: Path = Path(__name__).absolute().parent.joinpath("src")
    STATIC_ROOT: Path = ROOT_DIR.joinpath("static")
    TEMPLATES_ROOT: Path = ROOT_DIR.joinpath("templates")

    POSTGRES_URI_ALCHEMY: str = (
        "postgresql+asyncpg://{username}:{password}@{host}:{port}/{db_name}".format(
            username=getenv("POSTGRES_USERNAME", default="postgres"),
            password=getenv("POSTGRES_PASSWORD", default="postgres"),
            host=getenv("POSTGRES_HOST", default="localhost"),
            port=getenv("POSTGRES_PORT", default=5432),
            db_name=getenv("POSTGRES_DB", default="postgres"),
        )
    )

    POSTGRES_URI_SQL: str = (
        "postgres://{username}:{password}@{host}:{port}/{db_name}".format(
            username=getenv("POSTGRES_USERNAME", default="postgres"),
            password=getenv("POSTGRES_PASSWORD", default="postgres"),
            host=getenv("POSTGRES_HOST", default="localhost"),
            port=getenv("POSTGRES_PORT", default=5432),
            db_name=getenv("POSTGRES_DB", default="postgres"),
        )
    )
    MIN_SIZE: int = 10
    MAX_SIZE: int = 100
    POOLS_COUNT: int = 2


settings = Settings()
