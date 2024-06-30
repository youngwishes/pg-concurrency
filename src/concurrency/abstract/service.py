import abc
from sqlalchemy import ScalarResult
from concurrency.domains.entity import BaseEntity
from concurrency.abstract.repo import IRepository


class IService(abc.ABC):
    def __init__(self, repo: IRepository) -> None:
        self._repo = repo

    @abc.abstractmethod
    async def map(self, instance: ScalarResult) -> BaseEntity:
        """Маппинг результата запроса в БД на Pydantic сущность."""
