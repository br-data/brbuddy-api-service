"""Request models for BRBuddy backend requests."""

from typing import Mapping, Optional
from pydantic import BaseModel


class RequestModel(BaseModel):
    """API request model"""

    question: str
    context: Optional[Mapping] = None
    assistant_id: Optional[str] = None
    history: Optional[str] = None
