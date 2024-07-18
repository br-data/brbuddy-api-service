import os
from typing import Optional

from langchain_core.messages import HumanMessage
from langchain_core.documents.base import Document
from langchain_openai import AzureChatOpenAI

#from config import AZURE_OPENAI_API_KEY, AZURE_OPENAI_API_VERSION, AZURE_ENDPOINT, AZURE_OPENAI_DEPLOYMENT


#os.environ["AZURE_OPENAI_API_KEY"] = "***REMOVED***"
##os.environ["AZURE_OPENAI_ENDPOINT"] = "https://hackathon-openai-1.openai.azure.com/openai/deployments/alt-text-gpt-4/chat/completions"
#os.environ["AZURE_OPENAI_ENDPOINT"] = "https://hackathon-openai-1.openai.azure.com"
#os.environ["AZURE_OPENAI_API_VERSION"] = "2024-02-15-preview"
#os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT_NAME"] = "chat"

#model = AzureChatOpenAI(
#    openai_api_version=os.environ["AZURE_OPENAI_API_VERSION"],
#    azure_deployment=os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT_NAME"],
#)
#
#def generate_answer(question: str, context: list[Optional[Document]]) -> str:
#    message = HumanMessage(
#        content="Translate this sentence from English to French. I love programming."
#    )
#    print(model.invoke([message]))
#    return "test"
#
#
#if __name__ == "__main__":
#    generate_answer("bal", [])
#