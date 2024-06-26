from enum import Enum


class IsolationEnum(Enum):
    READ_COMMITED: int = 2
    REPEATABLE_READ: int = 3
    SERIALIZABLE: int = 4
