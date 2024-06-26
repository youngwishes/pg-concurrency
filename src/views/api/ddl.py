from starlette.responses import RedirectResponse
from starlette import status
from fastapi import Depends, APIRouter

from gateways.orders.providers.ddl import OrderProvider as DDLProvider
from depends.database.ddl import resolve_order_ddl_provider

router = APIRouter()


@router.post(
    "/schema/create",
    status_code=status.HTTP_201_CREATED,
    name="db:create-db-schema",
    response_class=RedirectResponse,
    description="Создание таблиц в БД.",
)
async def create_database_schema(
    provider: DDLProvider = Depends(resolve_order_ddl_provider),
) -> RedirectResponse:
    await provider.create_db_schema()
    return RedirectResponse("/index", status_code=status.HTTP_302_FOUND)


@router.post(
    "/schema/delete",
    status_code=status.HTTP_201_CREATED,
    name="db:drop-db-schema",
    response_class=RedirectResponse,
    description="Удаление таблиц из БД",
)
async def drop_database_schema(
    provider: DDLProvider = Depends(resolve_order_ddl_provider),
) -> RedirectResponse:
    await provider.drop_db_schema()
    return RedirectResponse("/index", status_code=status.HTTP_302_FOUND)
