from __future__ import annotations
from typing import Sequence, TYPE_CHECKING
from pydantic import BaseModel
import abc

if TYPE_CHECKING:
    from asyncpg import Pool
    from orders.domains.query import OrderQueries
    from core.lifespan_events import LogConnection
    from orders.abstract.provider import IQueryProvider
    from orders.abstract.callback import IQueryLogCallback


class IQuery(abc.ABC, BaseModel):
    """Базовый класс для параметров запроса."""


class IQueryResult(abc.ABC, BaseModel):
    """Базовый класс для результата запроса."""


class IQueryHandler(abc.ABC):
    """Базовый класс сервиса запросов."""

    def __init__(
        self,
        pools: Sequence[Pool],
        provider: IQueryProvider,
        callback: IQueryLogCallback,
    ) -> None:
        self.pools = pools
        self.provider = provider
        self.callback = callback

    def update_query_loggers(
        self, queries: OrderQueries, connections: Sequence[LogConnection]
    ) -> None:
        for conn, query, worker in zip(
            connections, (queries.first, queries.second), (1, 2)
        ):
            conn.remove_query_loggers()
            conn.add_query_logger(self.callback(query=query, worker=worker))

    @abc.abstractmethod
    async def handle(self, query: IQuery) -> IQueryResult:
        """Логика обработки запроса."""
