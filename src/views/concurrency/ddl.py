from starlette.responses import RedirectResponse
from starlette import status
from fastapi import Depends, APIRouter

from depends.concurrency.database import resolve_concurrency_service
from domains.concurrency.dto import PGSettingsDTO
from domains.concurrency.service import ConcurrencyService
from gateways.orders.providers.ddl import OrderProvider as DDLProvider
from depends.orders.ddl import resolve_order_ddl_provider

router = APIRouter()


@router.post(
    "/schema/create",
    status_code=status.HTTP_201_CREATED,
    name="ddl:create-db-schema",
    response_class=RedirectResponse,
    description="Создание таблиц в БД.",
)
async def create_database_schema(
    provider: DDLProvider = Depends(resolve_order_ddl_provider),
    service: ConcurrencyService = Depends(resolve_concurrency_service),
) -> RedirectResponse:
    await provider.create_db_schema()
    await service.update_settings(PGSettingsDTO(is_schema_created=True))
    return RedirectResponse("/index", status_code=status.HTTP_302_FOUND)


@router.post(
    "/schema/delete",
    status_code=status.HTTP_201_CREATED,
    name="ddl:drop-db-schema",
    response_class=RedirectResponse,
    description="Удаление таблиц из БД",
)
async def drop_database_schema(
    provider: DDLProvider = Depends(resolve_order_ddl_provider),
    service: ConcurrencyService = Depends(resolve_concurrency_service),
) -> RedirectResponse:
    await provider.drop_db_schema()
    await service.update_settings(PGSettingsDTO(is_schema_created=False))
    return RedirectResponse("/index", status_code=status.HTTP_302_FOUND)
