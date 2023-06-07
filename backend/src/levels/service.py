from typing import List

from sqlalchemy.orm import Session

from . import models, schemas


def get_levels(db: Session) -> List[models.Level]:
    return db.query(models.Level).all()


def create_level(db: Session, level: schemas.LevelCreate):
    # fake_hashed_password = user.password + "notreallyhashed"
    db_level = models.Level(**level.dict())
    db.add(db_level)  # add that instance object to your database session
    db.commit()  # commit the changes to the database (so that they are saved).
    db.refresh(db_level)  # refresh instance so that it contains any new data from the database, like the generated ID
    return db_level


# def get_level(db: Session, level_id: int):
#     return db.query(models.Level).filter(models.Level.id == level_id).first()


def get_level_by_name(db: Session, name: str):
    return db.query(models.Level).filter(models.Level.name == name).first()
