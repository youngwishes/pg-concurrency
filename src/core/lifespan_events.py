from fastapi import FastAPI

from core.enums import PostgresInterfaceEnum
from src.core.settings import Settings
import asyncpg
from asyncpg.connection import Connection


class LogConnection(Connection):
    def remove_query_loggers(self) -> None:
        self._query_loggers.clear()


async def db_create_connection_pools(app: FastAPI, settings: Settings) -> None:
    pools = []
    for _ in range(settings.POOLS_COUNT):
        pool = await asyncpg.create_pool(
            settings.resolve_postgres_uri(PostgresInterfaceEnum.ASYNCPG),
            min_size=10,
            max_size=100,
            statement_cache_size=0,
            connection_class=LogConnection,
        )
        pools.append(pool)
    app.state.db_pools = pools


async def db_close_connection_pools(app: FastAPI) -> None:
    for pool in app.state.db_pools:
        await pool.close()
