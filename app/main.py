from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.nlp import Sentiment


class Message(BaseModel):
    input: str
    output: str = ""  # None


app = FastAPI()
sentiment = Sentiment()

# origins = ["http://localhost", "http://localhost:3000", "http://127.0.0.1:3000"]

app.add_middleware(
    CORSMiddleware,
    # allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)


@app.post("/sentiment/")
async def sentiment_analysis(message: Message):
    message.output = str(sentiment.analyze(message.input))
    return {"output": message.output}
