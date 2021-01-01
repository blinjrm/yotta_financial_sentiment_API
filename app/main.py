from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.nlp import Sentiment


class Message(BaseModel):
    input: str
    output: str = ""  # None


app = FastAPI()
sentiment = Sentiment()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)


@app.post("/sentiment/")
async def sentiment_analysis(message: Message):
    message.output = str(sentiment.analyze(message.input))
    return {"output": message.output}
