import re
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import streamlit as st

model_name = "csebuetnlp/mT5_multilingual_XLSum"
tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=False, legacy=False)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

st.title("Генерация краткого содержания текста")

article_text = st.text_input("Введите текст для анализа")


WHITESPACE_HANDLER = lambda k: re.sub('\s+', ' ', re.sub('\n+', ' ', k.strip()))

input_ids = tokenizer(
    [WHITESPACE_HANDLER(article_text)],
    return_tensors="pt",
    padding="max_length",
    truncation=True,
    max_length=512
)["input_ids"]

output_ids = model.generate(
    input_ids=input_ids,
    max_length=84,
    no_repeat_ngram_size=2,
    num_beams=4
)[0]

summary = tokenizer.decode(
    output_ids,
    skip_special_tokens=True,
    clean_up_tokenization_spaces=False
)
if article_text:
    if article_text:
        st.subheader("Краткое содержание:")
        st.subheader(summary, divider='rainbow')
