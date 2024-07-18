from typing import Mapping, Optional, Union
from pydantic import BaseModel

from langchain_core.messages import HumanMessage, SystemMessage


class RequestModel(BaseModel):
    question: str
    context: Optional[Mapping] = None
    assistant_id: Optional[str] = None
    history: Optional[str] = None