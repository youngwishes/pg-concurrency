from orders.abstract.callback import IQueryLogCallback


class QueryLogCallback(IQueryLogCallback):
    def check_log_rules(self, query: str) -> bool:
        return (
            query.startswith("BEGIN")
            or query.startswith("COMMIT")
            or query.startswith("ROLLBACK")
        )

    def build_log_message(self, **kwargs) -> str:
        return "WorkerID - {worker}\n{record}\n{query}\n--".format(
            worker=kwargs["worker"],
            record=kwargs["record"],
            query=kwargs["query"],
        )
