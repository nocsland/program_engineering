from fastapi import FastAPI

from image_to_text.router import router as router_image_to_text
from question_answerer.router import router as router_question_answerer
from summary_text.router import router as  router_summary_text

app = FastAPI(
    title="Common api"
)

app.include_router(router_image_to_text)
app.include_router(router_question_answerer)
app.include_router(router_summary_text)
