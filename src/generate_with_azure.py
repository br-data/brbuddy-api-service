import os
from typing import Optional

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.documents.base import Document
from langchain_openai import AzureChatOpenAI


MODEL = AzureChatOpenAI(
    openai_api_version="2024-02-15-preview",
    azure_deployment="Hackathon-GPT4O",
)

SYSTEM_PROMPT = (
    "Du hilfst Mitarbeitenden beim Bayerischen Rundfunk bei ihren Fragen rund um den BR. "
    "Die bist ein bayerisches Uhrgestein. "
    "Dein Name ist 'Buddy'. "
    "Du fragst nach, wenn Fragen zu allgemein formuliert sind, um so die Anwort einzugrenzen. "
    "Du erfindest niemals Antworten. "
    "Du bist immer freundlich und geduldigt. "
    "Du erklärst in einfachen Worten."
)


def generate_answer(prompt: str, system_prompt: str = SYSTEM_PROMPT) -> str:
    message = SystemMessage(
        content=system_prompt
    )
    message = HumanMessage(
        content=prompt
    )
    result = MODEL.invoke([message])
    return result.content


if __name__ == "__main__":
    generate_answer("bal")
