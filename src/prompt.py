from typing import Optional
from langchain_core.documents.base import Document


# template to be filled with retrieved facts as bulletpoints and the user question
RAG_PROMPT_TEMPLATE = (
    "Beantworte die Frage nur auf Basis der folgenden Fakten und bringe keine eigenes Wissen ein. Formuliere die Fakten nur als Antwort um:"
    "\n\n"
    "{bulletpoints}"
    "\n\n"
    "Frage: {question}"
)


def assemble_prompt(
    question: str,
    context: list[Optional[Document]],
    template: str = RAG_PROMPT_TEMPLATE,
) -> str:
    """Assemble prompt to answer user question with LLM.

    :param question: user question
    :param context: retrieved facts that are related to the user question
    :param template: rag prompt template to use

    """
    # add retrieved facts
    bulletpoints = "\n- ".join([c.page_content.replace("\n", "") for c in context])
    bulletpoints = f"- {bulletpoints}"
    # assemble prompt
    return template.format(bulletpoints=bulletpoints, question=question)
