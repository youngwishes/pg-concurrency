from fastapi import APIRouter
from fastapi.responses import JSONResponse
from domains.concurrency.queries import ConcurrentQuery

router = APIRouter()


@router.post(
    "/make-sql-query",
    name="dml:make-sql-query",
    description="Сделать SQL запрос.",
    response_model=ConcurrentQuery,
)
async def make_sql_query(query: ConcurrentQuery) -> JSONResponse:
    return JSONResponse(content=query.model_dump())
