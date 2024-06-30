from enum import Enum


class PostgresInterfaceEnum(str, Enum):
    ASYNCPG: str = "asyncpg"
    SQL_ALCHEMY: str = "sql_alchemy"


class IsolationEnum(str, Enum):
    READ_COMMITTED: str = "read_committed"
    REPEATABLE_READ: str = "repeatable_read"
    SERIALIZABLE: str = "serializable"
