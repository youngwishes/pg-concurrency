from sqlalchemy import Integer, Boolean, Enum
from sqlalchemy.orm import Mapped, mapped_column

from core.database import Base
from core.enums import IsolationEnum


class PGConcurrencySettings(Base):
    __tablename__ = "concurrency"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    is_schema_created: Mapped[bool] = mapped_column(
        "Создана ли схема таблиц в БД.",
        Boolean,
        default=False,
    )
    is_db_populated: Mapped[bool] = mapped_column(
        "Наполнена ли БД",
        Boolean,
        default=False,
    )
    isolation_level: Mapped[IsolationEnum] = mapped_column(
        "Текущий уровень изоляции",
        Enum(IsolationEnum, name="isolation"),
        default=IsolationEnum.READ_COMMITTED,
    )
