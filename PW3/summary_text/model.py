from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "csebuetnlp/mT5_multilingual_XLSum"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=False, legacy=False)


def load_model():
    return pipeline("summarization", model=model, tokenizer=tokenizer)
