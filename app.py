"""Petit service FastAPI qui appelle une API de LLM (DeepSeek, format OpenAI)."""
import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from openai import OpenAI
from pydantic import BaseModel

load_dotenv()

MODELE = os.getenv("LLM_MODEL", "deepseek-chat")

app = FastAPI(title="Service LLM")


class Question(BaseModel):
    question: str


def get_client() -> OpenAI:
    cle = os.environ.get("DEEPSEEK_API_KEY")
    if not cle:
        raise HTTPException(status_code=500, detail="DEEPSEEK_API_KEY manquante")
    return OpenAI(api_key=cle, base_url="https://api.deepseek.com")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/ask")
def ask(corps: Question):
    reponse = get_client().chat.completions.create(
        model=MODELE,
        messages=[{"role": "user", "content": corps.question}],
    )
    return {"reponse": reponse.choices[0].message.content}
