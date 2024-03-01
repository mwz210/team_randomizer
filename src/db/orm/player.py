from typing import Any, Optional
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from enum import Enum
from pydantic import BaseModel

SQL_BASE: Any = declarative_base()


class PlayerDB(SQL_BASE):
    __tablename__: str = "players"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    position = Column(String)
    height = Column(Float)
    tier = Column(Integer)


class Player(BaseModel):
    first_name: str
    last_name: str
    height: float
    player_type: str


class PlayerFilter(BaseModel):
    first_name_contains: Optional[str] = None
