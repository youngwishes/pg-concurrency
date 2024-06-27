from typing import AsyncGenerator

from asyncpg import Pool, Connection
from fastapi import Request, Depends

from gateways.orders.providers.ddl import OrderProvider
from gateways.orders.queries import ddl_queries


async def _get_orders_db_pools(request: Request) -> list[Pool]:
    return request.app.state.db_pools


async def _resolve_order_ddl_connection(
    pools: list[Pool] = Depends(_get_orders_db_pools),
) -> AsyncGenerator[Connection, None]:
    async with pools[0].acquire() as connection:
        yield connection


async def resolve_order_ddl_provider(
    connection: Connection = Depends(_resolve_order_ddl_connection),
) -> OrderProvider:
    return OrderProvider(
        connection=connection,
        queries=ddl_queries,
    )
