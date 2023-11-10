"""

Постановка задачи описана тут: image_to_text_app/README.md

Необходимые зависимости: transformers, sentencepiece, streamlit, torch
Установка: pip install transformers sentencepiece streamlit torch

"""

import io
from PIL import Image

import streamlit as st
from transformers import BlipProcessor, BlipForConditionalGeneration

@st.cache_resource
def load_model(name):
    # загружаем\получаем из кэша модель
    return BlipForConditionalGeneration.from_pretrained(name)

def load_image():
    # формы для загрузки изображения
    uploaded_file = st.file_uploader(label='Выберите изображение')
    
    if uploaded_file is not None:
        # получение загруженного изображения
        image_data = uploaded_file.getvalue()
        
        # показ загруженного изображения
        st.image(image_data)
        
        # возврат конвертированного изображения
        return Image.open(io.BytesIO(image_data)).convert('RGB')
    else:
        return None

def main():
    # выводим заголовок страницы
    st.title('Генерация описания по изображению.')

    # вызываем функцию создания формы загрузки изображения
    img = load_image()
    
    # загружаем предварительно обученную модель
    model = load_model('Salesforce/blip-image-captioning-base')
    
    # создаём процессор
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")

    if img is not None:
        res = st.button('Сгенерировать описание')

        if res:
            inputs = processor(img, return_tensors="pt")
            
            out = model.generate(**inputs)
            st.write('*Результат (eng):*  :green[{}]'.format(processor.decode(out[0], skip_special_tokens=True).capitalize()))

if __name__ == "__main__":
    main()
