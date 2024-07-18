from typing import Optional, Generator
from langchain_core.documents.base import Document

from interface.response_models import CTA, CTAType
from urllib import parse


def generate_cta(context: list[Optional[Document]]) -> Generator[CTA, None, None]:
    for c in context:
        norm_name = parse.quote_plus(c.metadata['title'])
        yield CTA(
            type=CTAType.LINK,
            text=c.metadata["title"],
            payload=f"https://brbuddy-api-service-volume.brdata-dev.de/share/URV7wHnY/{norm_name}"
        )

