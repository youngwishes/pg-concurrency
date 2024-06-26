from fastapi import Request, APIRouter, Depends
from fastapi.responses import HTMLResponse
from starlette.templating import Jinja2Templates
from depends.jinja.templates import get_templates


router = APIRouter()


@router.get("/index", response_class=HTMLResponse)
async def index(
    request: Request, templates: Jinja2Templates = Depends(get_templates)
) -> HTMLResponse:
    context = {"created": True if request.headers.get("created") else False}
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context=context,
    )
