from enum import Enum


class IsolationEnum(str, Enum):
    READ_COMMITTED: str = "read_committed"
    REPEATABLE_READ: str = "repeatable_read"
    SERIALIZABLE: str = "serializable"
