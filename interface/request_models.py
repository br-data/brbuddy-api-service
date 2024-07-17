from typing import Mapping, Optional
from pydantic import BaseModel


class RequestModel(BaseModel):
    question: str
    context: Optional[Mapping] = None
    assistant_id: Optional[str] = None