from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.nlp import Sentiment


class Headline(BaseModel):
    input: str
    output: str = None


app = FastAPI()
sentiment = Sentiment()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)


@app.post("/")
def sentiment_analysis(headline: Headline):
    headline.output = str(sentiment.analyze(headline.input))
    return headline.output
