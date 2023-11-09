# DialogGPT-small-bot
В рамках выполнения работ по первой практической рабте была применена готовая модель https://huggingface.co/tinkoff-ai/ruDialoGPT-small

Данную модель можно использовать в развлекательных целях и с целью понять, как работают подобные модели.

[Открыть пример работы в Google Colab](https://colab.research.google.com/drive/1ECJdpJK24u7HrauriR8b-_ag7FjRdoOl#scrollTo=tO0RNt3cgDhB)

# Пример работы модели:
Ввести свой вопрос в диалог и получить ответ на него:
inputs = tokenizer('@@ПЕРВЫЙ@@ привет @@ВТОРОЙ@@ привет @@ПЕРВЫЙ@@ как дела? @@ВТОРОЙ@@', return_tensors='pt')

# Необходимые зависимости:
transformers sentencepiece

# Установка зависимостей:
!pip install transformers sentencepiece
