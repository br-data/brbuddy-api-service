
from typing import Optional
from langchain_core.documents.base import Document


RAG_PROMPT_TEMPLATE = (
    "Beantworte die Frage nur auf Basis der folgenden Fakten und bringe keine eigenes Wissen ein. Formuliere die Fakten nur als Antwort um:"
    "\n\n"
    "{bulletpoints}"
    "\n\n"
    "Frage: {question}"
)


def assemble_prompt(question: str, context: list[Optional[Document]], template: str = RAG_PROMPT_TEMPLATE) -> str:
    bulletpoints = "\n- ".join([c.page_content.replace("\n", "") for c in context])
    bulletpoints = f"- {bulletpoints}"
    return template.format(
        bulletpoints=bulletpoints,
        question=question
    )

