# Question answering model
---

Применена готовая модель https://huggingface.co/timpal0l/mdeberta-v3-base-squad2

Эту модель можно использовать для ответов на экстрактивные вопросы,\
т.е. учитывая вопрос и некоторый контекст, ответом будет является фрагмент из контекста.

[Открыть пример работы в Google Colab](https://colab.research.google.com/github/nocsland/program_engineering/blob/master/PW1/question_answerer_model/question_answerer_model.ipynb)

Пример работы модели:

    Enter your question: Как зовут собаку?
    Enter context: Когда мы взяли ее из приюта, то дали ей кличку Жучка

    question: Как зовут собаку?
    answer:  Жучка
    score:   0.9929
    start:   46
    end:     52
start - индекс первого символа ответа\
end - индекс последнего символа ответа