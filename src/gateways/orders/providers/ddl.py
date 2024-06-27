from core.orders.abstract.providers.ddl import DDLProvider


class OrderProvider(DDLProvider):
    async def create_db_schema(self) -> None:
        await self._queries.create_db_schema(self._connection)  # noqa

    async def drop_db_schema(self) -> None:
        await self._queries.drop_db_schema(self._connection)  # noqa
