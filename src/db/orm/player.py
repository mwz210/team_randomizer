from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from enum import Enum
from pydantic import BaseModel

SQL_BASE = declarative_base()


class PlayerDB(SQL_BASE):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    position = Column(String)
    height = Column(Float)
    tier = Column(Integer)


class Player(BaseModel):
    name: str
    height: float
    player_type: str


class PlayerFilter(BaseModel):
    pass
