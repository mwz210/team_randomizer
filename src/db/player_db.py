# crud/player.py

from dataclasses import dataclass
from functools import lru_cache
from typing import Any, Iterator, List, Optional
from fastapi import Query
from psycopg2 import DatabaseError
from sqlalchemy import URL, Engine, create_engine
from sqlalchemy.orm import Session, sessionmaker, declarative_base

from src.db.orm.player import Player, PlayerFilter, PlayerDB
from src.core.config import db_settings


@lru_cache(maxsize=None)
def get_engine(db_string: str | URL) -> Engine:
    return create_engine(db_string, pool_pre_ping=True)


class PlayerRepository:  # Interface
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def save(self, player: Player) -> None:
        raise NotImplementedError()

    def get_by_name(self, key: str) -> Optional[Player]:
        raise NotImplementedError()

    def get(self, player_filter: PlayerFilter) -> List[Player]:
        raise NotImplementedError()

    def get_all(self) -> List[Player]:
        raise NotImplementedError()


class SQLPlayerRepository(PlayerRepository):  # SQL Implementation of interface
    def __init__(self, session) -> None:
        self._session: Session = session

    def __exit__(self, exc_type, exc_value: str, exc_traceback: str) -> None:
        if any([exc_type, exc_value, exc_traceback]):
            self._session.rollback()
            return

        try:
            self._session.commit()
        except DatabaseError as e:
            self._session.rollback()
            raise e

    def save(self, player: Player) -> None:
        name_split: List = player.name.split(" ")
        self._session.add(
            PlayerDB(
                first_name=name_split[0],
                last_name=name_split[1],
                position=player.position,
                height=player.height,
            )
        )

    def get_by_name(self, name: str) -> Optional[Player]:
        instance: PlayerDB | None = (
            self._session.query(PlayerDB).filter(PlayerDB.name == name).first()
        )

        if instance:
            return Player()(key=instance.key, value=instance.value, done=instance.done)

        return None

    def get_all(self) -> List[PlayerDB]:
        query: Query[PlayerDB] = self._session.query(PlayerDB)
        return [
            Player(
                name=f"{player.first_name} {player.last_name}",
                height=player.height,
                player_type=player.position,
            )
            for player in query
        ]

    # def get(self, player_filter: PlayerFilter) -> List[Player]:
    #     query = self._session.query(PlayerDB())

    #     if player_filter.key_contains is not None:
    #         query = query.filter(PlayerDB.key.contains(PlayerDB.key_contains))

    #     if player_filter.value_contains is not None:
    #         query = query.filter(PlayerDB.value.contains(PlayerDB.value_contains))

    #     if player_filter.done is not None:
    #         query = query.filter(PlayerDB.done == PlayerDB.done)

    #     if player_filter.limit is not None:
    #         query = query.limit(PlayerDB.limit)

    #     return [Player()(key=todo.key, value=todo.value, done=todo.done) for todo in query]


def create_player_repository() -> Iterator[PlayerRepository]:
    url: URL = URL.create(
        drivername="postgresql",
        username=db_settings.user,
        password=db_settings.password,
        host=db_settings.host,
        database=db_settings.database,
        port=db_settings.port,
    )
    session: Session = sessionmaker(bind=get_engine(url))()
    player_repository = SQLPlayerRepository(session)

    try:
        yield player_repository
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
