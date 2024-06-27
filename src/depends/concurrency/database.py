from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.concurrency.database import get_session
from domains.concurrency.service import ConcurrencyService
from gateways.concurrency.repo import ConcurrencyRepo


async def _get_concurrency_repo(
    session: AsyncSession = Depends(get_session),
) -> ConcurrencyRepo:
    return ConcurrencyRepo(session=session)


async def resolve_concurrency_service(
    repo: ConcurrencyRepo = Depends(_get_concurrency_repo),
) -> ConcurrencyService:
    return ConcurrencyService(repo=repo)
