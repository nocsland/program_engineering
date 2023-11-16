# API генерации описания по изображению (image to text model), используя FastAPI

## Постановка задачи:

Реализовать простое API, используя фреймворк `FastAPI` и предварительно обученную модель из `HuggingFace`.

## Решение:

Применена готовая модель: https://huggingface.co/Salesforce/blip-image-captioning-base

Модель предварительно обученная на наборе данных COCO — базовая архитектура (с базовой магистралью ViT) и применима для условных и безусловных подписей к изображениям. 

### Запуск приложения:

1) Создать виртуальное окружение:
```
    python3 -m venv env
```
2) Активировать виртуальное окружение:
```
    source env/bin/activate
```
3) Перейти в `program_engineering/PW3/image_to_text`
```
    cd program_engineering/PW3/image_to_text
```
4) Установить зависимости:
```
    pip install -r requirements.txt
```
5) Вернуться в директорию с файлом main.py
```
    cd ../
```
6.1) Запустить приложение:
```
    uvicorn main:app --reload
```
6.2) Запустить приложение на своём порте (например: 5007):
```
    uvicorn main:app --reload --port 5007
```

### Работа с API:
1) Через документацию FastAPI:

- открыть в браузере страницу с документацией `http://domain:port/docs`, где `domain` и `port` ваш домен и порт, где запущено приложение
- открыть роут `/image_to_text/` POST запрос
- нажать кнопку `Try in out`
- загрузить файл
- нажать кнопку `Execute`

2) Через стороннего клиента (например: Insomnia):

- сформировать POST запрос с заголовком `Content-Type: multipart/form-data`
- указать имя тела сообщения - `file`
- тело сообщения - `путь до вашего файла`
- отправить запрос на `http://domain:port/image_to_text`, где `domain` и `port` ваш домен и порт, где запущено приложение

### Пример ответа (Response body):

```
"Результат (eng): A man in a hard hat looking at something"
```
