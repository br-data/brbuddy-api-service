from pydantic import BaseModel
from typing import Mapping, Any


class ResponseModel(BaseModel):
    answer: str
    refs: list[str]
    status: str
    msg: str
    cta: list[Any]
