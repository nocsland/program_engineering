# Text to image model

## Постановка задачи:

Написать `ImageCreator` для создания изображений на основе текста, используя готовую модель `HuggingFace`.

## Решение:

Написан минимальный класс `ImageCreator` с возможностью расширения в любой плоскости.

Применена готовая модель: https://huggingface.co/runwayml/stable-diffusion-v1-5

`Stable Diffusion` — это скрытая модель диффузии текста в изображение, способная генерировать фотореалистичные изображения при любом вводе текста.

[Открыть пример работы в Google Colab](https://colab.research.google.com/github/nocsland/program_engineering/blob/master/PW1/text_2_image_model/text_2_image_model.ipynb)

### Пример работы модели:
```
    Enter prompt: big sun at night
    Enter file name: big_sun_at_night.png
```

Результат выполнения: сгенерированное изображение (big_sun_at_night.png), сохранённое в дирректорию с проектом.

### Необходимые зависимости:
```
    transformers
    sentencepiece
    diffusers
```
### Установка зависимостей:
```
    pip install transformers sentencepiece diffusers
```
