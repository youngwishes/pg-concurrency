from core.entity import BaseEntity
from core.enums import IsolationEnum
from pydantic import Field


class PGSettingsEntity(BaseEntity):
    is_schema_created: bool = Field(..., description="Созданы ли таблицы в БД.")
    isolation_level: IsolationEnum = Field(
        IsolationEnum.READ_COMMITED, description="Текущий уровень изоляции транзакций."
    )
