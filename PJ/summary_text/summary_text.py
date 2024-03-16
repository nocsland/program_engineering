import streamlit as st
from chardet import detect
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import pipeline


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

def detect_encoding(data: bytes) -> str:
    """Return encoding"""
    return detect(data)["encoding"]


if __name__ == "__main__":
    # запускаем приложение
    main()
