from fastapi import FastAPI
from src.core.settings import Settings
import asyncpg


async def db_create_connection_pools(app: FastAPI, settings: Settings) -> None:
    pools = []
    for _ in range(settings.POOLS_COUNT):
        pool = await asyncpg.create_pool(
            settings.POSTGRES_URI_SQL,
            min_size=10,
            max_size=100,
            statement_cache_size=0,
        )
        pools.append(pool)
    app.state.db_pools = pools


async def db_close_connection_pools(app: FastAPI) -> None:
    for pool in app.state.db_pools:
        await pool.close()
