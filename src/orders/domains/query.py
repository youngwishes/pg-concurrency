from typing import final
from orders.abstract.query import IQuery, IQueryHandler
import asyncio


@final
class OrderQueries(IQuery):
    first: str
    second: str


class OrderQueryHandler(IQueryHandler):
    async def handle(self, queries: OrderQueries) -> None:
        connections = [await pool.acquire() for pool in self.pools]

        result = await asyncio.gather(
            *[
                self.provider.make(query=sql, connection=conn)
                for conn, sql in zip(connections, (queries.first, queries.second))
            ],
            return_exceptions=True,
        )
        print(result)
        for pool in self.pools:
            await asyncio.wait_for(await pool.close(), timeout=10)
