import io
from PIL import Image

from transformers import BlipProcessor, BlipForConditionalGeneration

async def load_model():
    # загружаем\получаем модель
    return BlipForConditionalGeneration.from_pretrained('Salesforce/blip-image-captioning-base')
