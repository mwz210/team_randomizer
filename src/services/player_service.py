from db import player_db


def create_player(db: Session, player: schemas.PlayerCreate) -> Any:
    db_player = models.Player(**player.dict())
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player


def get_player(db: Session, player_id: int) -> Any | None:
    return db.query(models.Player).filter(models.Player.id == player_id).first()


def get_player_by_name(db: Session, player_name: str) -> Any | None:
    return db.query(models.Player).filter(models.Player.name == player_name).first()


def get_player(db: Session) -> List:
    return db.query(models.Player).all()


# Define other CRUD functions (update, delete, etc.) similarly
