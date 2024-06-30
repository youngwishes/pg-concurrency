import abc
import logging
from typing import Callable

from asyncpg.connection import LoggedQuery


class IQueryLogCallback(abc.ABC):
    def __init__(self):
        self.logger = logging.getLogger("concurrency")

    @abc.abstractmethod
    def check_log_rules(self, query: str) -> bool:
        """Определяет, какие логи из PostgreSQL нужно писать в журнал."""

    @abc.abstractmethod
    def build_log_message(self, **kwargs) -> str:
        """Формирование сообщения для логирования в журнал."""

    def __call__(self, query: str, worker: int) -> Callable:
        def wrapper(record: LoggedQuery) -> None:
            if self.check_log_rules(record.query):
                message = self.build_log_message(
                    worker=worker, record=record.query, query=query
                )
                self.logger.info(message)

        return wrapper
