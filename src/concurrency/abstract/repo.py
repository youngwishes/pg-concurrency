from __future__ import annotations
from typing import Sequence, Any, TYPE_CHECKING
import abc

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession
    from concurrency.domains.dto import BaseDTO


class IRepository(abc.ABC):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    @abc.abstractmethod
    async def create(self, model: BaseDTO) -> Any:
        """Создать новую запись в БД."""

    @abc.abstractmethod
    async def update(self, model: BaseDTO) -> Any:
        """Обновить запись по уникальному идентификатору."""

    @abc.abstractmethod
    async def fetch_all(self) -> Sequence[Any]:
        """Получить все записи из БД."""
