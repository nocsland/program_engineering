from fastapi import APIRouter, Depends
from pydantic import BaseModel

from PW5.summary_text.src.model import load_model

router = APIRouter(
    prefix="/summary_text",
    tags=["SummaryText"]
)


class Item(BaseModel):
    text: str

@router.get("/")
async def base_page():
    """
    Возвращает приветственное сообщение
    """
    return {"message": "Welcome to Base Page"}

@router.post("/")
async def summary_text(
        item: Item,
        model=Depends(load_model),
):
    """
    Генерирует краткое содержание введенного текста
    """
    try:
        # генерация ответа
        result = model(item.text)

        return {
            "Краткое содержание:": result[0]['summary_text'],

        }

    except Exception as e:
        return {"Error message": e.__str__()}
