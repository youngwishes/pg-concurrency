from pydantic import Field, BaseModel
from core.enums import IsolationEnum


class BaseEntity(BaseModel):
    id: int

    class Config:
        from_attributes = True


class PGSettingsEntity(BaseEntity):
    is_schema_created: bool = Field(..., description="Созданы ли таблицы в БД.")
    isolation_level: IsolationEnum = Field(
        IsolationEnum.READ_COMMITTED, description="Текущий уровень изоляции транзакций."
    )
    is_db_populated: bool = Field(None, description="Наполнена ли БД данными.")
