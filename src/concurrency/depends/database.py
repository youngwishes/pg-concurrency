from __future__ import annotations
from typing import TYPE_CHECKING
from fastapi import Depends
from core.database import get_session
from concurrency.domains.service import ConcurrencyService
from concurrency.gateways.repo import ConcurrencyRepo


if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


async def _get_concurrency_repo(
    session: AsyncSession = Depends(get_session),
) -> ConcurrencyRepo:
    return ConcurrencyRepo(session=session)


async def resolve_concurrency_service(
    repo: ConcurrencyRepo = Depends(_get_concurrency_repo),
) -> ConcurrencyService:
    return ConcurrencyService(repo=repo)
