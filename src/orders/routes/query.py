from fastapi import APIRouter, Depends
from fastapi.responses import RedirectResponse
from starlette import status

from orders.depends.query import resolve_query_handler
from orders.domains.query import OrderQueries, OrderQueryHandler

router = APIRouter()


@router.post(
    "/make-sql-query",
    name="dml:make-sql-query",
    description="Сделать SQL запрос.",
    response_model=OrderQueries,
)
async def make_sql_query(
    queries: OrderQueries, handler: OrderQueryHandler = Depends(resolve_query_handler)
) -> RedirectResponse:
    await handler.handle(queries=queries)
    return RedirectResponse("/index", status_code=status.HTTP_302_FOUND)
