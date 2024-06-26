from sqlalchemy import Integer, Boolean, SmallInteger
from sqlalchemy.orm import declarative_base, sessionmaker, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from core.enums import IsolationEnum
from core.settings import settings

Base = declarative_base()

engine = create_async_engine(
    settings.POSTGRES_URI_ALCHEMY,
    echo=True,
    future=True,
)

SessionMaker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_session() -> AsyncSession:
    async with SessionMaker() as session:
        yield session


class PostgresConcurrencySettings(Base):
    __tablename__ = "concurrency"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    is_schema_created: Mapped[bool] = mapped_column(
        "Создана ли схема таблиц в БД.",
        Boolean,
        default=False,
    )
    isolation_level: Mapped[int] = mapped_column(
        "Текущий уровень изоляции",
        SmallInteger,
        default=IsolationEnum.READ_COMMITED,
    )
