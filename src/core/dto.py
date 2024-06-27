from pydantic import BaseModel
from typing import Optional


class BaseDTO(BaseModel):
    id: Optional[int] = None
