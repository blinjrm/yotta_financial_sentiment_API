from typing import List

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.nlp import Sentiment


app = FastAPI()
sentiment = Sentiment()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)


@app.post("/")
def sentiment_analysis(headlines: List[str]):
    predictions = []

    for headline in headlines:
        prediction = sentiment.analyze(headline)
        predictions.append(prediction)

    return predictions
