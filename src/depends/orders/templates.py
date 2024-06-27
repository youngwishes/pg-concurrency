from starlette.templating import Jinja2Templates
from core.settings import settings


def get_templates() -> Jinja2Templates:
    return Jinja2Templates(directory=str(settings.TEMPLATES_ROOT))
