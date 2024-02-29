from typing import List
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from src.core.config import settings

from src.api.router import router


app = FastAPI(
    title=settings.title,
    version=settings.version,
    description=settings.description,
    openapi_prefix=settings.api_prefix,
    docs_url=settings.docs_url,
    openapi_url=settings.openapi_url,
)

app.include_router(router, prefix=settings.api_prefix)


@app.get("/")
async def root() -> dict[str, str]:
    return RedirectResponse(app.docs_url)
