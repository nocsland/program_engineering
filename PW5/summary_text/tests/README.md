### Список тестов

1. GET. test_get_base_page. Базовая страница приложения. Проверяет статус-код и возвращаемое сообщение.
2. POST. test_post_eng_text. Отправка текста на английском языке. Проверяет статус-код и возврат краткого содержания
   текста.
3. POST. test_post_rus_text. Отправка короткого текста на русском языке. Проверяет статус-код и возврат тестового
   резюме.
4. POST. test_post_empty_string. Отправка пустой строки. Проверяет статус-код и возврат сообщения по умолчанию для
   пустой строки.
5. POST. test_error_empty_json. Отправка пустого JSON. Проверяет статус-код и возврат ошибки.

### Текущий статус

[![Python application](https://github.com/nocsland/program_engineering/actions/workflows/python-app.yml/badge.svg)](https://github.com/nocsland/program_engineering/actions/workflows/python-app.yml)