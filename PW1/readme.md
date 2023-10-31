в рамках этого практического задания подключили модель https://huggingface.co/csebuetnlp/mT5_multilingual_XLSum

Функционал модели:
Генерирует резюме текстовой статьи, исходя из текста.

Важно:
для запуска лучше использовать https://colab.research.google.com/?hl=ru  т.к. на локальной машине использует много
ресресурсов для установки библиотек и т.п.

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