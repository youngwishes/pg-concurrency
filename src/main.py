from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from typing import AsyncGenerator
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from core.lifespan_events import db_create_connection_pools, db_close_connection_pools
from core.settings import settings

from concurrency.routes.frontend import router as fronted_router
from concurrency.routes.schema import router as schema_router
from orders.routes.query import router as query_router


@asynccontextmanager
async def lifespan(application: FastAPI) -> AsyncGenerator:
    await db_create_connection_pools(application, settings)

    yield

    await db_close_connection_pools(application)


def create_app() -> FastAPI:
    application = FastAPI(
        title="Postgres Concurrency",
        lifespan=lifespan,
        docs_url="/docs",
    )
    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
        allow_credentials=True,
    )
    application.mount(
        str(settings.STATIC_ROOT),
        StaticFiles(directory=str(settings.STATIC_ROOT)),
        name="static",
    )
    application.include_router(fronted_router, tags=["Frontend"])
    application.include_router(schema_router, tags=["Schema"])
    application.include_router(query_router, tags=["Query"])

    return application


app = create_app()
