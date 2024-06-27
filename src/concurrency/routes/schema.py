from starlette.responses import RedirectResponse
from starlette import status
from fastapi import Depends, APIRouter

from concurrency.depends.database import resolve_concurrency_service
from concurrency.domains.dto import PGSettingsDTO
from concurrency.domains.service import ConcurrencyService
from orders.gateways.providers.schema import OrderSchemaProvider
from orders.depends.provider import resolve_schema_provider

router = APIRouter(prefix="/schema")


@router.post(
    "/create",
    status_code=status.HTTP_201_CREATED,
    name="concurrency:create-db-schema",
    response_class=RedirectResponse,
    description="Создание таблиц в БД.",
)
async def create_database_schema(
    provider: OrderSchemaProvider = Depends(resolve_schema_provider),
    service: ConcurrencyService = Depends(resolve_concurrency_service),
) -> RedirectResponse:
    await provider.create_db_schema()
    await service.update_settings(
        PGSettingsDTO(is_schema_created=True, is_db_populated=False)
    )
    return RedirectResponse("/index", status_code=status.HTTP_302_FOUND)


@router.post(
    "/delete",
    status_code=status.HTTP_201_CREATED,
    name="concurrency:drop-db-schema",
    response_class=RedirectResponse,
    description="Удаление таблиц из БД",
)
async def drop_database_schema(
    provider: OrderSchemaProvider = Depends(resolve_schema_provider),
    service: ConcurrencyService = Depends(resolve_concurrency_service),
) -> RedirectResponse:
    await provider.drop_db_schema()
    await service.update_settings(
        PGSettingsDTO(is_schema_created=False, is_db_populated=True)
    )
    return RedirectResponse("/index", status_code=status.HTTP_302_FOUND)


@router.post(
    "/populate",
    status_code=status.HTTP_201_CREATED,
    name="concurrency:populate-db",
    response_class=RedirectResponse,
    description="Наполнить БД",
)
async def populate_db(
    provider: OrderSchemaProvider = Depends(resolve_schema_provider),
    service: ConcurrencyService = Depends(resolve_concurrency_service),
) -> RedirectResponse:
    await provider.populate()
    await service.update_settings(PGSettingsDTO(is_db_populated=True))
    return RedirectResponse("/index", status_code=status.HTTP_302_FOUND)
