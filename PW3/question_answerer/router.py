from fastapi import APIRouter, Depends
from pydantic import BaseModel

from question_answerer.model import load_model


router = APIRouter(
    prefix="/question_answerer",
    tags=["QuestionAnswerer"]
)

class Item(BaseModel):
    context: str
    question: str

@router.post("/")
async def question_answerer(
    item: Item,
    model = Depends(load_model),
):
    """
    использовать для ответов на экстрактивные вопросы,
    т.е. учитывая вопрос и некоторый контекст, ответом будет является фрагмент из контекста
    """
    try:
        # генерация ответа
        result = model(item.question, item.context)

        return {
                "ответ": result['answer'],
                "оценка результата": round(result['score'], 4),
                "индекс первого символа ответа": result['start'],
                "индекс последнего символа ответа": result['end']
                }

    except Exception as e:
        return {"Error message": e.__str__()}
