import os
from typing import Optional, Union, Tuple

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.documents.base import Document
from langchain_openai import AzureChatOpenAI


MODEL = AzureChatOpenAI(
    openai_api_version="2024-02-15-preview",
    azure_deployment="Hackathon-GPT4O",
    temperature=0,
    max_tokens=500,
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


def generate_answer(
    prompt: str,
    history: list[Optional[Union[SystemMessage, HumanMessage]]],
    system_prompt: str = SYSTEM_PROMPT,
    max_len: int = 500,
    temperature: int = 0,
    top_p: float = 0.5
) -> Tuple[str, list[Union[SystemMessage, HumanMessage]]]:
    if not history:
        history.append(
            SystemMessage(
                content=system_prompt
            )
        )
    history.append(HumanMessage(content=prompt))
    result = MODEL.invoke(history)
    return result.content, history


if __name__ == "__main__":
    generate_answer("bal")
