from pydantic import Field, BaseModel
from typing import Optional
from core.enums import IsolationEnum


class BaseDTO(BaseModel):
    id: Optional[int] = None


class PGSettingsDTO(BaseDTO):
    is_schema_created: Optional[bool] = Field(
        None, description="Созданы ли таблицы в БД."
    )
    isolation_level: Optional[IsolationEnum] = Field(
        None, description="Текущий уровень изоляции транзакций."
    )
    is_db_populated: Optional[bool] = Field(
        None, description="Наполнена ли БД данными."
    )
