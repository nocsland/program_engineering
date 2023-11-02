"""
Пример использования пайплайна готовой модели машинного обучения.

Применена модель https://huggingface.co/timpal0l/mdeberta-v3-base-squad2
"""


from transformers import pipeline


question_answerer = pipeline("question-answering",
                             model="timpal0l/mdeberta-v3-base-squad2")


if __name__ == "__main__":
    question = input("Enter your question: ")
    context = input("Enter context: ")

    preds = question_answerer(question, context)

    print(f"\nquestion: {question}\n\
    answer: {preds['answer']}\n\
    score:\t{round(preds['score'], 4)},\n\
    start:\t{preds['start']},\n\
    end:\t{preds['end']}")
