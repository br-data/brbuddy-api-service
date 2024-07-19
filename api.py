"""API proxy enpoints for BRBuddy application."""
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
import uvicorn

from langchain.load.dump import dumps
from langchain.load.load import loads

from interface.response_models import ResponseModel, CTAType
from interface.request_models import RequestModel
from src.context import get_context
from src.tools import generate_cta
from src.generate_with_azure import generate_answer
# from src.generate_with_openai import generate_answer
from src.prompt import assemble_prompt


APP = FastAPI(
    title="BRBuddy Backend",
    description="Proxy for the microsoft hackathon",
    version="0.0.1",
)

ORIGINS = [
    "https://interaktiv.brdata-dev.de",
    "https://interaktiv.br.de",
    "http://localhost:8080",
    "http://localhost",
    "http://0.0.0.0:8080",
    "http://0.0.0.0",
]

APP.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@APP.get("/")
async def redirect():
    """Redirect to documentation if index page is called."""
    response = RedirectResponse(url="/docs")
    return response


@APP.post("/v1/answer_question", response_model=ResponseModel)
def answer_a_question(query: RequestModel) -> ResponseModel:
    """Answre a question by using a RAG enriched LLM generation approach."""
    # If a chat history exists, then load and resume it.
    # Otherwise start new history.
    if query.history is not None:
        history = loads(query.history)
    else:
        history = []

    # get RAG context
    context = get_context(query.question)
    prompt = assemble_prompt(query.question, context)
    answer, history = generate_answer(prompt, history)
    # collect the source reference handles
    refs = [c.metadata["title"] for c in context]
    return ResponseModel(
        status="ok",
        msg="Successfully generated answer",
        answer=answer,
        cta=list(generate_cta(context)),  # assemble 'call to actions'
        refs=refs,
        history=dumps(history),  # return history as string
    )


if __name__ == "__main__":
    uvicorn.run(APP, host="0.0.0.0", port=3000)
