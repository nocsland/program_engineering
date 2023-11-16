from PIL import Image


async def load_image(data):
    # чтение изображения и конвертация в RGB
    return Image.open(data).convert('RGB')
