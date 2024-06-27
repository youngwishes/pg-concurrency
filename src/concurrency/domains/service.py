from concurrency.abstract.service import AbstractService
from core.enums import IsolationEnum
from concurrency.domains.dto import PGSettingsDTO
from concurrency.domains.entity import PGSettingsEntity
from concurrency.gateways.models import PostgresConcurrencySettings


class ConcurrencyService(AbstractService):
    async def update_settings(self, settings: PGSettingsDTO) -> PGSettingsEntity:
        result = await self._repo.update(settings)
        return await self.map(result)

    async def fetch_current_settings(self) -> PGSettingsEntity:
        result = await self._repo.fetch_all()
        if len(result) == 0:
            result = await self._repo.create(
                PGSettingsDTO(
                    is_schema_created=False,
                    isolation_level=IsolationEnum.READ_COMMITTED,
                    is_db_populated=False,
                )
            )
        else:
            result = result[0]
        return await self.map(result)

    async def map(self, instance: PostgresConcurrencySettings) -> PGSettingsEntity:
        return PGSettingsEntity(
            id=instance.id,
            is_schema_created=instance.is_schema_created,
            isolation_level=instance.isolation_level,
            is_db_populated=instance.is_db_populated,
        )
