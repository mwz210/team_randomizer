from fastapi import APIRouter

from src.api.routes.players import router as players_router

router = APIRouter()


router.include_router(players_router, prefix="/players")
