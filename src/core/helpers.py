import logging
from typing import Callable

from fastapi import Depends
from core.enums import IsolationEnum
from concurrency.depends.database import resolve_concurrency_service
from concurrency.domains.service import ConcurrencyService


logger = logging.getLogger("concurrency")


async def get_isolation_level(
    service: ConcurrencyService = Depends(resolve_concurrency_service),
) -> IsolationEnum:
    settings = await service.fetch_current_settings()
    return settings.isolation_level


def in_journal(func: Callable) -> Callable:
    async def wrapper(*args, **kwargs) -> None:
        logger.info("------Transactions Started------\n")
        result = await func(*args, **kwargs)
        logger.info(f"------Transactions Completed------\nResult: {result}")
        return result

    return wrapper
