import abc
from typing import Sequence, Any
from sqlalchemy.ext.asyncio import AsyncSession
from core.dto import BaseDTO


class AbstractRepository(abc.ABC):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    @abc.abstractmethod
    async def fetch_one(self, pk: int | str) -> Any:
        """Выбрать запись по уникальному идентификатору."""

    @abc.abstractmethod
    async def update(self, model: BaseDTO) -> Any:
        """Обновить запись по уникальному идентификатору."""

    @abc.abstractmethod
    async def create(self, model: BaseDTO) -> Any:
        """Создать новую запись в БД."""

    @abc.abstractmethod
    async def fetch_all(self) -> Sequence[Any]:
        """Получить все записи из БД."""
