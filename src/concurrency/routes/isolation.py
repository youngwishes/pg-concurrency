from starlette.responses import RedirectResponse
from starlette import status
from fastapi import Depends, APIRouter

from concurrency.depends.database import resolve_concurrency_service
from concurrency.domains.dto import PGSettingsDTO
from concurrency.domains.service import ConcurrencyService
from core.enums import IsolationEnum

router = APIRouter(prefix="/isolation")


@router.post(
    "/rc",
    status_code=status.HTTP_201_CREATED,
    name="concurrency:set-rc-isolation",
    response_class=RedirectResponse,
    description="Изменить уровень изоляции на READ COMMITTED.",
)
async def set_read_committed(
    service: ConcurrencyService = Depends(resolve_concurrency_service),
) -> RedirectResponse:
    await service.update_settings(
        PGSettingsDTO(isolation_level=IsolationEnum.READ_COMMITTED)
    )
    return RedirectResponse("/index", status_code=status.HTTP_302_FOUND)


@router.post(
    "/rr",
    status_code=status.HTTP_201_CREATED,
    name="concurrency:set-rr-isolation",
    response_class=RedirectResponse,
    description="Изменить уровень изоляции на REPEATABLE READ.",
)
async def set_repeatable_read(
    service: ConcurrencyService = Depends(resolve_concurrency_service),
) -> RedirectResponse:
    await service.update_settings(
        PGSettingsDTO(isolation_level=IsolationEnum.REPEATABLE_READ)
    )
    return RedirectResponse("/index", status_code=status.HTTP_302_FOUND)


@router.post(
    "/ser",
    status_code=status.HTTP_201_CREATED,
    name="concurrency:set-ser-isolation",
    response_class=RedirectResponse,
    description="Изменить уровень изоляции на SERIALIZABLE.",
)
async def set_serializable(
    service: ConcurrencyService = Depends(resolve_concurrency_service),
) -> RedirectResponse:
    await service.update_settings(
        PGSettingsDTO(isolation_level=IsolationEnum.SERIALIZABLE)
    )
    return RedirectResponse("/index", status_code=status.HTTP_302_FOUND)
