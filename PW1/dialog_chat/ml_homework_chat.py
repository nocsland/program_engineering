"""
Пример использования пайплайна готовой модели машинного обучения.

Применена модель https://huggingface.co/tinkoff-ai/ruDialoGPT-small
"""
import torch
from transformers import AutoTokenizer, AutoModelWithLMHead
tokenizer = AutoTokenizer.from_pretrained('tinkoff-ai/ruDialoGPT-small')
model = AutoModelWithLMHead.from_pretrained('tinkoff-ai/ruDialoGPT-small')
inputs = tokenizer('@@ПЕРВЫЙ@@ привет @@ВТОРОЙ@@ привет @@ПЕРВЫЙ@@ кто ты? @@ВТОРОЙ@@', return_tensors='pt')
generated_token_ids = model.generate(
    **inputs,
    top_k=10,
    top_p=0.95,
    num_beams=3,
    num_return_sequences=3,
    do_sample=True,
    no_repeat_ngram_size=2,
    temperature=1.2,
    repetition_penalty=1.2,
    length_penalty=1.0,
    eos_token_id=50257,
    max_new_tokens=40
)
context_with_response = [tokenizer.decode(sample_token_ids) for sample_token_ids in generated_token_ids]
context_with_response
