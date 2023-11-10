# Генерация описания по изображению (image to text model)

## Постановка задачи:

Реализовать простое приложение, используя фреймворк `Streamlit` и предварительно обученную модель из `HuggingFace`.

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
3) Запуск приложения: 

- 3.1 Для применения стилей перейти в `program_engineering/PW2/image_to_text_app`

```
    cd program_engineering/PW2/image_to_text_app
```
- 3.2 Запустить:

```
    streamlit run image_to_text_app.py
```

### Работа с приложением:
1) Загрузить изображение
2) Нажать кнопку "Сгенерировать описание"

### Пример ответа:

```
Результат (eng): A man in a hard hat looking at something
```

### Необходимые зависимости:
```
    transformers
    sentencepiece
    streamlit 
    torch
```
### Установка зависимостей:
```
    pip install transformers sentencepiece streamlit torch
```
