from typing import List
from fastapi import FastAPI
from src.core.config import settings

from src.api.router import router


app = FastAPI(
    title=settings.title,
    version=settings.version,
    description=settings.description,
    openapi_prefix=settings.api_prefix,
    docs_url=settings.docs_url,
    openapi_url=settings.openapi_url
)

app.include_router(router, prefix=settings.api_prefix)


@app.get("/")
async def root() -> dict[str, str]:
    return {"Say": "Hello!"}


@app.get("/players")
async def get_players() -> List:
    pass

@app.post("/players/{player_id}")
async def post_player(player_id: str) -> None:
    pass

