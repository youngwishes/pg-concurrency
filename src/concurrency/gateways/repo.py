from __future__ import annotations
from typing import Sequence, TYPE_CHECKING
from sqlalchemy import select, insert, update
from concurrency.gateways.models import PGConcurrencySettings
from concurrency.abstract.repo import IRepository

if TYPE_CHECKING:
    from concurrency.domains.dto import BaseDTO


class ConcurrencyRepo(IRepository):
    async def fetch_all(self) -> Sequence[PGConcurrencySettings]:
        async with self._session.begin():
            result = await self._session.execute(
                select(PGConcurrencySettings).order_by(PGConcurrencySettings.id)
            )
        return result.scalars().all()

    async def create(self, model: BaseDTO) -> PGConcurrencySettings:
        async with self._session.begin():
            result = await self._session.execute(
                insert(PGConcurrencySettings)
                .values(**model.model_dump(exclude={"id"}, exclude_none=True))
                .returning(PGConcurrencySettings)
            )
        return result.scalar_one()

    async def update(self, model: BaseDTO) -> PGConcurrencySettings:
        async with self._session.begin():
            result = await self._session.execute(
                update(PGConcurrencySettings)
                .values(**model.model_dump(exclude={"id"}, exclude_none=True))
                .returning(PGConcurrencySettings)
            )
        return result.scalar_one()
