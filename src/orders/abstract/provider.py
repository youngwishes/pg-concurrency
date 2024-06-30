import abc
from aiosql.queries import Queries
from asyncpg import Connection

from core.enums import IsolationEnum


class ISchemaProvider(abc.ABC):
    def __init__(self, connection: Connection, queries: Queries) -> None:
        self._connection = connection
        self._queries = queries

    @abc.abstractmethod
    async def create_db_schema(self) -> None:
        """Создание таблиц."""

    @abc.abstractmethod
    async def drop_db_schema(self) -> None:
        """Удаление таблиц."""


class IQueryProvider(abc.ABC):
    def __init__(self, isolation: IsolationEnum) -> None:
        self.isolation = isolation

    @abc.abstractmethod
    async def make(
        self,
        query: str,
        connection: Connection,
    ) -> None:
        """Выполнить SQL запрос."""
