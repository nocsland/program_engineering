В рамках этого практического задания подключили модель https://huggingface.co/csebuetnlp/mT5_multilingual_XLSum

Функционал модели:
Генерирует резюме текстовой статьи, исходя из текста на 45 языках.

Последовательность действий для проверки работы модели:

1. Перейти на https://colab.research.google.com/?hl=ru
2. Войти в аккаунт google
3. "Файл" -> Открыть блокнот
4. Выбрать репозиторий https://github.com/nocsland/program_engineering
5. Загрузить файл ноутбука summary_text.ipynb из каталога PW1
6. При первом запуске запустить последовательно обе ячейки
7. При втором и последующем использовании достаточно запускать только ячейку с моделью
8. После запуска модели в поле "Введите текст" необходимо ввести исходный текст и нажать "Enter"
9. После обработки введенного текста будет выведена надпись "Краткое содержание введенного текста:" и резюме текста
   Пример работы модели можно увидеть по ссылке: 
https://colab.research.google.com/github/nocsland/program_engineering/blob/master/PW1/summary_text_model/summary_text.ipynb?hl=ru#scrollTo=9wQyDdAQ-3GV

Загрузить готовый jupyter notebook с подключенной моделью можно из
гитхаба https://github.com/nocsland/program_engineering/blob/master/PW1/summary_text_model/summary_text.ipynb

Важно:
Для запуска рекомендуется использовать google colab https://colab.research.google.com/?hl=ru  т.к. на локальной машине
модель использует много ресурсов для установки библиотек и т.п.

Если возникает ошибка:
ValueError: Couldn't instantiate the backend tokenizer from one of:
(1) a `tokenizers` library serialization file,
(2) a slow tokenizer instance to convert or
(3) an equivalent slow tokenizer class to instantiate and convert.
You need to have sentencepiece installed to convert a slow tokenizer to a fast one. site:stackoverflow.com

Необходимо:

1. Деинсталлировать стандартный модуль transformers командой pip uninstall transformers
2. Установить модуль другой модуль !pip install --no-cache-dir transformers sentencepiece
3. Использовать Use_fast=False в конструкции tokenizer = AutoTokenizer.from_pretrained(“XXXXX”, use_fast=False)

Пункты 2-3 добавлены в файл ноутбука summary_text.ipynb.