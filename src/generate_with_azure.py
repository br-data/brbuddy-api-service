from typing import Optional, Union, Tuple

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import AzureChatOpenAI


# load LLM for the generation of the answer based on the rag prompt
MODEL = AzureChatOpenAI(
    openai_api_version="2024-02-15-preview",
    azure_deployment="Hackathon-GPT4O",
    temperature=0,
    max_tokens=500,
)

# system prompt setting the general functionality of the LLM behavior
SYSTEM_PROMPT = (
    "Du hilfst Mitarbeitenden beim Bayerischen Rundfunk bei ihren Fragen rund um den BR. "
    "Die bist ein bayerisches Urgestein. "
    "Dein Name ist 'BR Buddy'. "
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
    top_p: float = 0.5,
) -> Tuple[str, list[Union[SystemMessage, HumanMessage]]]:
    """Generate a answer related to the user prompt.

    :param prompt: rag prompt
    :param history: chat history
    :param system_prompt: to set general behavior of the llm answer
    :param max_len: max number of tokens in the answer
    :param temperature: creativity setting for the llm
    :param top_p: variation of the top tokens probabilities, considered in generation
    """
    # only add system prompt if not present in the chat history
    if not history:
        history.append(SystemMessage(content=system_prompt))
    # add rag prompt that includes the user question
    history.append(HumanMessage(content=prompt))
    # generate answer
    result = MODEL.invoke(history)
    # return answer string
    return result.content, history
