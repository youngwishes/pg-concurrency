from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from typing import AsyncGenerator
from core.lifespan_events import db_create_connection_pools, db_close_connection_pools
from core.settings import settings
from views.interface.index import router as html_router
from views.api.ddl import router as ddl_router
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(application: FastAPI) -> AsyncGenerator:
    await db_create_connection_pools(application, settings)

    yield

    await db_close_connection_pools(application)


def create_app() -> FastAPI:
    application = FastAPI(
        title="pg_concurrency",
        lifespan=lifespan,
        docs_url="/docs",
    )
    application.mount(
        str(settings.STATIC_ROOT),
        StaticFiles(directory=str(settings.STATIC_ROOT)),
        name="static",
    )
    application.include_router(html_router)
    application.include_router(ddl_router)

    return application


app = create_app()
