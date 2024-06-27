from asyncpg import Connection
from orders.abstract.provider import IQueryProvider


class OrderQueryProvider(IQueryProvider):
    async def make(self, query: str, connection: Connection) -> None:
        async with connection.transaction():
            await connection.cursor(query=query)
