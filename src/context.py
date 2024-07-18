import os

os.environ["AZURESEARCH_FIELDS_ID"] = "chunk_id"
os.environ["AZURESEARCH_FIELDS_CONTENT"] = "chunk"
os.environ["AZURESEARCH_FIELDS_CONTENT_VECTOR"] = "text_vector"

from typing import Any, Optional

from langchain_community.vectorstores.azuresearch import AzureSearch
from langchain_openai import AzureOpenAIEmbeddings, OpenAIEmbeddings
from langchain_core.documents.base import Document

from config import (
    AZURE_ENDPOINT,
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_API_VERSION,
    AZURE_DEPLOYMENT,
    VECTOR_STORE_ADDRESS,
    VECTOR_STORE_PASSWORD,
    INDEX_NAME
)


EMBEDDINGS: AzureOpenAIEmbeddings = AzureOpenAIEmbeddings(
    azure_deployment=AZURE_DEPLOYMENT,
    #openai_api_version=azure_openai_api_version,
    azure_endpoint=AZURE_ENDPOINT,
    api_key=AZURE_OPENAI_API_KEY
)
VECTOR_STORE: AzureSearch = AzureSearch(
    azure_search_endpoint=VECTOR_STORE_ADDRESS,
    azure_search_key=VECTOR_STORE_PASSWORD,
    index_name=INDEX_NAME,
    embedding_function=EMBEDDINGS.embed_query
)

def get_context(
    query: str,
    k: int = 3,
    search_type: str = "hybrid"
) -> list[Optional[Document]]:
    context = []
    docs = VECTOR_STORE.similarity_search(
        query=query,
        k=3,
        search_type=search_type,
    )
    if docs is not None and docs:
        context.extend(docs)

    return context
