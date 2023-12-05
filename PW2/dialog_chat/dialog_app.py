import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelWithLMHead

tokenizer = AutoTokenizer.from_pretrained('tinkoff-ai/ruDialoGPT-small')
model = AutoModelWithLMHead.from_pretrained('tinkoff-ai/ruDialoGPT-small')

st.title('Проверка тестовой модели')

user_input = st.text_input("Введите ваш тест здесь:")

if user_input:
   inputs = tokenizer(user_input, return_tensors='pt')
   generated_token_ids = model.generate(
       **inputs,
       top_k=10,
       top_p=0.95,
       num_beams=3,
       num_return_sequences=1,
       do_sample=True,
       no_repeat_ngram_size=2,
       temperature=1.2,
       repetition_penalty=1.2,
       length_penalty=1.0,
       eos_token_id=50257,
       max_new_tokens=40
   )
   response = tokenizer.decode(generated_token_ids[0])
   st.write(f'Response: {response}')
