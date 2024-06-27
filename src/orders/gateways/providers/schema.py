from orders.abstract.provider import ISchemaProvider


class OrderSchemaProvider(ISchemaProvider):
    async def create_db_schema(self) -> None:
        await self._queries.create_db_schema(self._connection)  # noqa

    async def drop_db_schema(self) -> None:
        await self._queries.drop_db_schema(self._connection)  # noqa

    async def populate(self) -> None:
        await self._queries.populate(self._connection)  # noqa
