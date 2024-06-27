from asyncpg import Pool
from fastapi import Depends

from core.database import get_db_pools
from orders.domains.query import OrderQueryHandler
from orders.gateways.providers.query import OrderQueryProvider


async def _resolve_query_provider() -> OrderQueryProvider:
    return OrderQueryProvider()


async def resolve_query_handler(
    provider: OrderQueryProvider = Depends(_resolve_query_provider),
    pools: list[Pool] = Depends(get_db_pools),
) -> OrderQueryHandler:
    return OrderQueryHandler(
        pools=pools,
        provider=provider,
    )
