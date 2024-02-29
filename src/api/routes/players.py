from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from src.db.player_db import PlayerRepository, create_player_repository

from src.db.orm.player import Player

router = APIRouter()


@router.get(
    "",
    response_model=list[Player],
    status_code=status.HTTP_200_OK,
    name="get_players",
    tags=["players"],
)
async def get_players(
    player_repository: PlayerRepository = Depends(create_player_repository),
) -> list[Player]:
    with player_repository as repo:
        players: List[Player] = repo.get_all()
        if not players:
            raise HTTPException(status_code=404, detail="Players not found")

        return players
