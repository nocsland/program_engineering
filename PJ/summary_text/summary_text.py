import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import pipeline

model_name = "csebuetnlp/mT5_multilingual_XLSum"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name, legasy=False)


@st.cache_resource
def load_model():
    return pipeline("summarization", model=model, tokenizer=tokenizer)


summary_text = load_model()
st.title("Создание краткого резюме")
st.write("Вы можете использовать текст на любом из 43 языков")

source_button = st.radio(
    "\nВыберите источник данных",
    ["Ввод текста", "Загрузка файла"],
    captions=["Вставить текст из буфера или ввести с клавиатуры", "Загрузить текст из файла формата TXT"])
if source_button == "Ввод текста":
    text = st.text_area("Введите текст")
elif source_button == "Загрузка файла":
    uploaded_file = st.file_uploader("Выберите файл", type='txt', accept_multiple_files=False)
    if uploaded_file is not None:
        text = uploaded_file.read().decode()
    else:
        text = ""
button = st.button('Создать')
if button:
    try:
        st.markdown("**Результат:**")
        st.write(summary_text(text, max_length=200, min_length=50)[0]['summary_text'])
    except Exception as e:
        st.write(f"Ошибка: {e}")
