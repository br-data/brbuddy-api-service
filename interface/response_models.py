from pydantic import BaseModel
from typing import Mapping, Any
from enum import Enum


class CTAType(Enum):
  MAIL = "MAIL"
  CALL = "CALL"
  CITATION = "CITATION"
  LINK = "LINK"
  MEDIA = "MEDIA"
  TEAMS_CHAT = "TEAMS_CHAT"
  CALENDAR = "CALENDAR"


class CTA(BaseModel):
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
