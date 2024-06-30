import asyncio
import logging
from typing import final, Any
from core.helpers import in_journal
from orders.abstract.query import IQuery, IQueryHandler, IQueryResult

logger = logging.getLogger("concurrency")


@final
class OrderQueries(IQuery):
    first: str
    second: str


@final
class OrderQueriesResult(IQueryResult):
    first: Any
    second: Any


class OrderQueryHandler(IQueryHandler):
    @in_journal
    async def handle(self, queries: OrderQueries) -> OrderQueriesResult:
        async with self.pools[0].acquire() as first_connection:
            async with self.pools[1].acquire() as second_connection:
                self.update_query_loggers(
                    queries, (first_connection, second_connection)
                )
                result = await asyncio.gather(
                    *[
                        self.provider.make(query=sql, connection=conn)
                        for conn, sql in zip(
                            (first_connection, second_connection),
                            (queries.first, queries.second),
                        )
                    ],
                    return_exceptions=True,
                )
        return OrderQueriesResult(first=result[0], second=result[1])
