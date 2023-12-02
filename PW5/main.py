from fastapi import FastAPI

from PW5.summary_text.src.router import router as router_summary_text

app = FastAPI(
    title="Common api"
)

app.include_router(router_summary_text)
