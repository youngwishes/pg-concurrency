import abc
from typing import Sequence
from orders.abstract.provider import IQueryProvider
from asyncpg import Pool
from pydantic import BaseModel


class IQuery(abc.ABC, BaseModel):
    """Базовый класс для параметров запроса."""


class IQueryResult(abc.ABC, BaseModel):
    """Базовый класс для результата запроса."""


class IQueryHandler(abc.ABC):
    """Базовый класс сервиса запросов."""

    def __init__(self, pools: Sequence[Pool], provider: IQueryProvider) -> None:
        self.pools = pools
        self.provider = provider

    @abc.abstractmethod
    async def handle(self, query: IQuery) -> IQueryResult:
        """Логика обработки запроса."""
