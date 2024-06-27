from typing import AsyncGenerator

from asyncpg import Pool, Connection
from fastapi import Depends

from core.database import get_db_pools
from orders.gateways.providers.schema import OrderSchemaProvider
from orders.gateways.queries import orders_queries


async def _resolve_db_connection(
    pools: list[Pool] = Depends(get_db_pools),
) -> AsyncGenerator[Connection, None]:
    async with pools[0].acquire() as connection:
        yield connection


async def resolve_schema_provider(
    connection: Connection = Depends(_resolve_db_connection),
) -> OrderSchemaProvider:
    return OrderSchemaProvider(
        connection=connection,
        queries=orders_queries,
    )
