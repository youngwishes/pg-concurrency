from asyncpg import Pool
from fastapi import Depends
from core.database import get_db_pools
from core.enums import IsolationEnum
from core.helpers import get_isolation_level
from orders.domains.callback import QueryLogCallback
from orders.domains.query import OrderQueryHandler
from orders.gateways.providers.query import OrderQueryProvider


async def _resolve_query_callback() -> QueryLogCallback:
    return QueryLogCallback()


async def _resolve_query_provider(
    isolation: IsolationEnum = Depends(get_isolation_level),
) -> OrderQueryProvider:
    return OrderQueryProvider(isolation=isolation)


async def resolve_query_handler(
    pools: list[Pool] = Depends(get_db_pools),
    provider: OrderQueryProvider = Depends(_resolve_query_provider),
    callback: QueryLogCallback = Depends(_resolve_query_callback),
) -> OrderQueryHandler:
    return OrderQueryHandler(
        pools=pools,
        provider=provider,
        callback=callback,
    )
