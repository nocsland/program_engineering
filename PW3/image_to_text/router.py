from fastapi import APIRouter, Depends, File, UploadFile

from image_to_text.model import load_model
from image_to_text.processor import Processor
from image_to_text.utility import load_image


router = APIRouter(
    prefix="/image_to_text",
    tags=["ImageToText"]
)

@router.post("/")
async def get_text_from_image(
    file: UploadFile = File(...),
    model = Depends(load_model),
    processor = Depends(Processor),
):
    try:
        # чтение изображения
        img = await load_image(file.file)

        # генерация текстового описания
        result = await processor.process(img, model)

        return 'Результат (eng): {}'.format(result)

    except Exception as e:
        return {"Error message": e.__str__()}
    finally:
        file.file.close()
