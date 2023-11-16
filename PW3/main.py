from fastapi import FastAPI

from image_to_text.router import router as router_image_to_text

app = FastAPI(
    title="Common api"
)

app.include_router(router_image_to_text)
