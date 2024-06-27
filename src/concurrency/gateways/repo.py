from typing import Sequence

from sqlalchemy import select, insert, update

from concurrency.domains.dto import BaseDTO
from concurrency.gateways.models import PostgresConcurrencySettings
from concurrency.abstract.repo import AbstractRepository


class ConcurrencyRepo(AbstractRepository):
    async def fetch_one(self, pk: int | str) -> PostgresConcurrencySettings | None:
        result = await self._session.execute(
            select(PostgresConcurrencySettings).where(
                PostgresConcurrencySettings.id == pk
            )
        )
        return result.scalar_one_or_none()

    async def fetch_all(self) -> Sequence[PostgresConcurrencySettings]:
        result = await self._session.execute(
            select(PostgresConcurrencySettings).order_by(PostgresConcurrencySettings.id)
        )
        return result.scalars().all()

    async def create(self, model: BaseDTO) -> PostgresConcurrencySettings:
        result = await self._session.execute(
            insert(PostgresConcurrencySettings)
            .values(**model.model_dump(exclude={"id"}, exclude_none=True))
            .returning(PostgresConcurrencySettings)
        )
        await self._session.commit()
        return result.scalar_one()

    async def update(self, model: BaseDTO) -> PostgresConcurrencySettings:
        print(model.model_dump(exclude_none=True))
        result = await self._session.execute(
            update(PostgresConcurrencySettings)
            .values(**model.model_dump(exclude={"id"}, exclude_none=True))
            .returning(PostgresConcurrencySettings)
        )
        await self._session.commit()
        return result.scalar_one()
