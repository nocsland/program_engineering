import io
import streamlit as st
from transformers import pipeline

# Декоратор @st.cache говорит Streamlit, что модель нужно загрузить только один раз, чтобы избежать утечек памяти
@st.cache_resource
# загружает модель
def load_model():
    return pipeline("question-answering",
                    model="AndrewChar/model-QA-5-epoch-RU")



# Загружаем предварительно обученную модель
question_answerer = load_model()

# Выводим заголовок страницы средствами Streamlit
st.title('Question answering application')

st.write('Это приложение можно использовать для ответов на экстрактивные вопросы,\
т.е. учитывая вопрос и некоторый контекст, ответом будет является фрагмент из контекста.')

context = st.text_area('Контекст', 'Когда мы взяли ее из приюта, то дали ей кличку Жучка')

question = st.text_input('Вопрос', 'Как зовут собаку?')

# Показывам кнопку для запуска
result = st.button('Ответить на вопрос')
# Если кнопка нажата, то запускаем
if result:
    preds = question_answerer(question, context)

    # st.write('**Результаты распознавания:**')
    # st.write("question:", question)
    # st.write('context:', context)
    st.write("ответ:", preds['answer'])
    st.write("оценка результата:\t", round(preds['score'], 4))
    st.write("индекс первого символа ответа:\t", preds['start'])
    st.write("индекс последнего символа ответа:\t", preds['end'])
