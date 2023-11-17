import io
from transformers import pipeline


# загружает модель
def load_model():
    return pipeline("question-answering",
                    model="AndrewChar/model-QA-5-epoch-RU")
