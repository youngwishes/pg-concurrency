from typing import final
from core.concurrency.abstract.queries import IQuery


@final
class ConcurrentQuery(IQuery):
    first_sql: str
    second_sql: str
