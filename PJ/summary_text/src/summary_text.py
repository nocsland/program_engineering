from base64 import b64encode

import streamlit as st
from chardet import detect
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import pipeline


@st.cache_data
def get_base64(file: str) -> str:
    # загрузка файла в base64 для streamlit
    with open(file, "rb") as f:
        data = f.read()
    return b64encode(data).decode()


def set_background(file: str) -> None:
    # установка стилей фона для streamlit
    bin_str = get_base64(file)
    page_bg_img = '''
    <style>
    [class="appview-container st-emotion-cache-1wrcr25 ea3mdgi4"] {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    background-repeat:no-repeat;
    background-position: center center;
    }
    </style>
    ''' % bin_str

    st.markdown(page_bg_img, unsafe_allow_html=True)


@st.cache_resource
def load_model():
    # создание кэшированных объектов модели и токенайзера
    model_name = "csebuetnlp/mT5_multilingual_XLSum"
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name, legasy=False)

    # загружаем\получаем из кэша объект pipeline с моделью
    return pipeline("summarization", model=model, tokenizer=tokenizer)


def main():
    # загружаем предварительно обученную модель
    summary_text = load_model()
    # задаем переменную с текстом по умолчанию пустой
    text = ""

    # загрузка фона
    set_background("../static/image.png")

    # вывод заголовка
    st.title("Помощник студента")
    st.write("Приложение возвращает краткое содержание текста, поддерживает данные на нескольких языках.")

    # выбор источника данных
    source_button = st.radio(
        "Выберите источник данных",
        ["Ввод текста", "Загрузка файла"],
        captions=["Вставить текст из буфера или ввести с клавиатуры", "Загрузить текст из файла формата TXT"],
    )

    # форма ввода текста
    if source_button == "Ввод текста":
        text = st.text_area("Введите текст")

    elif source_button == "Загрузка файла":
        # форма для загрузки файла
        uploaded_file = st.file_uploader(
            "Выберите файл",
            type="txt",
            accept_multiple_files=False,
        )

        if uploaded_file is not None:
            # чтение текста из файла
            txt_bytes = uploaded_file.read()
            # определение кодировки
            encoding = detect_encoding(data=txt_bytes)
            # декодирование и вывод превью
            text = txt_bytes.decode(encoding=encoding, errors="ignore")
            text = st.text_area(
                label="Проверьте и при необходимости отредактируйте текст:",
                value=text,
            )
        else:
            text = ""

    length = len(text.split())

    # слайдер "Cтепень сжатия результата"
    brevity_level = st.slider(
        "Cтепень сжатия результата (10 - кратко, 100 - подробно)",
        min_value=10,
        max_value=100,
        value=50
    )

    # кнопка "Создать"
    button = st.button("Создать")
    if button and text:
        try:
            with st.spinner("Пожалуйста, подождите..."):
                # выводим результат
                st.markdown("**Результат: ** %s" % summary_text(
                    text,
                    max_length=round(length * 1.5),
                    min_length=round(length * (brevity_level / 100)))[0]["summary_text"],
                )
        except Exception as e:
            # выводим возникающие ошибки
            st.write(f"Ошибка: {e}")


def detect_encoding(data: bytes) -> str:
    """Return encoding"""
    return detect(data)["encoding"]


if __name__ == "__main__":
    # запускаем приложение
    main()
