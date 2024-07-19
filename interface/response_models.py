from pydantic import BaseModel
from typing import Any
from enum import Enum


class CTAType(Enum):
    """Call to action types."""

    MAIL = "MAIL"
    CALL = "CALL"
    CITATION = "CITATION"
    LINK = "LINK"
    MEDIA = "MEDIA"
    TEAMS_CHAT = "TEAMS_CHAT"
    CALENDAR = "CALENDAR"


class CTA(BaseModel):
    """Call to action object.

    Call to actions tell the frontend what to do with a specific source reference.
    """
    type: CTAType
    text: str
    payload: Any


class ResponseModel(BaseModel):
    answer: str
    refs: list[str]
    status: str
    msg: str
    cta: list[CTA]
    history: str
