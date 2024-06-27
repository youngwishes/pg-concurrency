import pathlib
import aiosql


orders_queries = aiosql.from_path(
    pathlib.Path(__file__).parent / "sql" / "orders.sql", "asyncpg"
)
