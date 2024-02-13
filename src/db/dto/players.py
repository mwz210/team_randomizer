from enum import Enum
from pydantic import BaseModel

class PlayerType(Enum):
    pass

class Height(BaseModel):
    pass


class Player(BaseModel):
    name: str
    height: Height
    player_type: PlayerType


    