from asyncpg import Pool
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from starlette.requests import Request

from core.settings import settings

Base = declarative_base()

engine = create_async_engine(
    settings.POSTGRES_URI_ALCHEMY,
    echo=True,
    future=True,
)

SessionMaker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)  # noqa


async def get_session() -> AsyncSession:
    async with SessionMaker() as session:
        yield session


async def get_db_pools(request: Request) -> list[Pool]:
    return request.app.state.db_pools
