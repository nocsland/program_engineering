import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import pipeline

model_name = "csebuetnlp/mT5_multilingual_XLSum"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name, legasy=False)


# Декоратор @st.cache говорит Streamlit, что модель нужно загрузить только один раз, чтобы избежать утечек памяти
@st.cache_resource
# загружает модель
def load_model():
    return pipeline("summarization", model=model, tokenizer=tokenizer)


# Загружаем предварительно обученную модель
summary_text = load_model()

# Выводим заголовок страницы
st.title("Генерация краткого содержания")

# Выбираем источник данных
source_button = st.radio(
    "Выберете источник данных",
    ["Ввод текста", "Загрузка файла"],
    captions=["Вставить текст из буфера, или ввести с клавиатуры", "Загрузить текст из файла формата .txt"])
if source_button == "Ввод текста":
    # Источник буфер или клавиатура
    text = st.text_area("Введите текст для анализа")
elif source_button == "Загрузка файла":
    # Источник файл .txt
    uploaded_files = st.file_uploader("Выберете .txt файлы", accept_multiple_files=True)
    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        text = bytes_data.decode()
# Создаем кнопку
button = st.button('Генерировать')

# Выводим результат по нажатию кнопки
if button:
    try:
        st.subheader("Краткое содержание:")
        st.write(summary_text(text)[0]['summary_text'])
    except NameError: st.write("File is empty")

