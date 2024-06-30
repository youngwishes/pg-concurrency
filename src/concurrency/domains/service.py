from __future__ import annotations
from typing import TYPE_CHECKING
from concurrency.abstract.service import IService
from concurrency.domains.dto import PGSettingsDTO
from concurrency.domains.entity import PGSettingsEntity
from core.enums import IsolationEnum


if TYPE_CHECKING:
    from concurrency.gateways.models import PGConcurrencySettings


class ConcurrencyService(IService):
    async def update_settings(self, pg_settings: PGSettingsDTO) -> PGSettingsEntity:
        result = await self._repo.update(pg_settings)
        return await self.map(result)

    async def fetch_current_settings(self) -> PGSettingsEntity:
        result = await self._repo.fetch_all()
        pg_settings = (
            result[0] if result else await self._repo.create(self.default_settings)
        )
        return await self.map(pg_settings)

    @property
    def default_settings(self) -> PGSettingsDTO:
        return PGSettingsDTO(
            isolation_level=IsolationEnum.READ_COMMITTED,
            is_db_populated=False,
            is_schema_created=False,
        )

    async def map(self, instance: PGConcurrencySettings) -> PGSettingsEntity:
        return PGSettingsEntity(
            id=instance.id,
            is_schema_created=instance.is_schema_created,
            isolation_level=instance.isolation_level,
            is_db_populated=instance.is_db_populated,
        )
