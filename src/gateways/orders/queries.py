import pathlib
import aiosql


ddl_queries = aiosql.from_path(
    pathlib.Path(__file__).parent / "sql" / "ddl.sql", "asyncpg"
)
