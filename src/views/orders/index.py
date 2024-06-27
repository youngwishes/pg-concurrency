from fastapi import Request, APIRouter, Depends
from fastapi.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from depends.concurrency.database import resolve_concurrency_service
from depends.orders.templates import get_templates
from domains.concurrency.service import ConcurrencyService

router = APIRouter()


@router.get("/index", response_class=HTMLResponse)
async def index(
    request: Request,
    templates: Jinja2Templates = Depends(get_templates),
    service: ConcurrencyService = Depends(resolve_concurrency_service),
) -> HTMLResponse:
    settings = await service.fetch_current_settings()
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context=settings.model_dump(exclude={"id"}, exclude_none=True),
    )
