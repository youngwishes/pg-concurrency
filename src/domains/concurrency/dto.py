from core.dto import BaseDTO
from pydantic import Field
from typing import Optional


class PGSettingsDTO(BaseDTO):
    is_schema_created: Optional[bool] = Field(
        None, description="Созданы ли таблицы в БД."
    )
    isolation_level: Optional[int] = Field(
        None, description="Текущий уровень изоляции транзакций."
    )
