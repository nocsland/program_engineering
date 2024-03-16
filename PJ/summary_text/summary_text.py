from base64 import b64encode

import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import pipeline


@st.cache_data
def get_base64(file: str) -> str:
    # загрузка файла в base64 для streamlit
    with open(file, 'rb') as f:
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
    
    # загрузка фона
    set_background("../static/image.png")

    st.title("Создание краткого резюме")
    st.write("Вы можете использовать текст на любом из 45 языков")

    # выбор источника данных
    source_button = st.radio(
        "\nВыберите источник данных",
        ["Ввод текста", "Загрузка файла"],
        captions=[
            "Вставить текст из буфера или ввести с клавиатуры",
            "Загрузить текст из файла формата TXT",
        ],
    )

    if source_button == "Ввод текста":
        text = st.text_area("Введите текст")

    elif source_button == "Загрузка файла":
        # форма для загрузки изображения
        uploaded_file = st.file_uploader(
            "Выберите файл",
            type="txt",
            accept_multiple_files=False,
        )

        if uploaded_file is not None:
            # чтение текста из файла
            text = uploaded_file.read().decode()
        else:
            text = ""

    button = st.button("Создать")

    if button:
        try:
            # выводим результат
            st.markdown("**Результат:**")
            st.write(summary_text(
                text,
                max_length=200,
                min_length=50,
            )[0]["summary_text"])

        except Exception as e:
            # выводим возникающие ошибки
            st.write(f"Ошибка: {e}")


if __name__ == "__main__":
    # запускаем приложение
    main()
