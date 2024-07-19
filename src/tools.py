from typing import Optional, Generator, Mapping, Union
from langchain_core.documents.base import Document
from langchain_core.messages import HumanMessage, SystemMessage
from interface.response_models import CTA, CTAType
from urllib import parse


def generate_cta(context: list[Optional[Document]]) -> Generator[CTA, None, None]:
    for c in context:
        norm_name = parse.quote_plus(c.metadata['title'])
        yield CTA(
            type=CTAType.LINK,
            text=c.metadata["title"],
            payload=f"https://storage.googleapis.com/brbuddy/{norm_name}"
        )
