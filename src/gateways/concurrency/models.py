from sqlalchemy import Integer, Boolean, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column

from core.concurrency.database import Base
from core.enums import IsolationEnum


class PostgresConcurrencySettings(Base):
    __tablename__ = "concurrency"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    is_schema_created: Mapped[bool] = mapped_column(
        "Создана ли схема таблиц в БД.",
        Boolean,
        default=False,
    )
    isolation_level: Mapped[int] = mapped_column(
        "Текущий уровень изоляции",
        SmallInteger,
        default=IsolationEnum.READ_COMMITED,
    )
