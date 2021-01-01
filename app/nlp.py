from transformers import RobertaForSequenceClassification, RobertaTokenizer, pipeline


class Sentiment:

    MODEL_NAME = "blinjrm/finsent"

    def __init__(self):
        self.classifier = pipeline(
            "sentiment-analysis",
            model=RobertaForSequenceClassification.from_pretrained(self.MODEL_NAME),
            tokenizer=RobertaTokenizer.from_pretrained(self.MODEL_NAME),
        )

    def analyze(self, headline: str):
        result = self.classifier(headline)[0]
        return f"label: {result['label']}, with score: {round(result['score'], 4)}"
