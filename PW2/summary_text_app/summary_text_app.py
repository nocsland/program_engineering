import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import pipeline

model_name = "csebuetnlp/mT5_multilingual_XLSum"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name, legasy=False)


# @st.cache модель нужно загрузить только один раз
@st.cache_resource
# загружает модель
def load_model():
    return pipeline("summarization", model=model, tokenizer=tokenizer)


# Загружаем предварительно обученную модель
summary_text = load_model()

# Выводим заголовок страницы
st.title("Генерация краткого содержания")
st.write("Вы можете использовать текст на любом из 43 языков")

# Выбираем источник данных
source_button = st.radio(
    "\nВыберете источник данных",
    ["Ввод текста", "Загрузка файла"],
    captions=["Вставить текст из буфера или ввести с клавиатуры", "Загрузить текст из файла формата TXT"])
if source_button == "Ввод текста":
    # Источник буфер или клавиатура
    text = st.text_area("Введите текст для анализа")
elif source_button == "Загрузка файла":
    # Источник файл TXT
    uploaded_file = st.file_uploader("Выберете файл", type='txt', accept_multiple_files=False)
    if uploaded_file is not None:
        text = uploaded_file.read().decode()
# Создаем кнопку
button = st.button('Генерировать')

# Выводим результат по нажатию кнопки
if button:
    try:
        st.subheader("Краткое содержание:")
        st.write(summary_text(text, max_length=200, min_length=50)[0]['summary_text'])
    except NameError:
        st.write("Файл не загружен")
