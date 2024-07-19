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
    INDEX_NAME,
)


# embeddings, compatible with the Azure search index
EMBEDDINGS: AzureOpenAIEmbeddings = AzureOpenAIEmbeddings(
    azure_deployment=AZURE_DEPLOYMENT,
    # openai_api_version=azure_openai_api_version,
    azure_endpoint=AZURE_ENDPOINT,
    api_key=AZURE_OPENAI_API_KEY,
)
# load the search index
# index was setup and is provided by the use of Azure Cloud tools
VECTOR_STORE: AzureSearch = AzureSearch(
    azure_search_endpoint=VECTOR_STORE_ADDRESS,
    azure_search_key=VECTOR_STORE_PASSWORD,
    index_name=INDEX_NAME,
    embedding_function=EMBEDDINGS.embed_query,
)


def get_context(
    query: str, k: int = 3, search_type: str = "hybrid"
) -> list[Optional[Document]]:
    """Search for RAG facts from the search index.

    :param query: user question to be answered
    :param k: number of facts to retrieve
    :param search_type: how to search for facts (semantic, hybrid, ...)
    """
    context = []
    # retrieve rag facts from the search index
    docs = VECTOR_STORE.similarity_search(
        query,
        k=k,
        search_type=search_type,
    )
    # add to return value
    if docs is not None and docs:
        context.extend(docs)

    return context
