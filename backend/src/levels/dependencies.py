# async def valid_post_id(post_id: UUID4) -> Mapping:
#     post = await service.get_by_id(post_id)
#     if not post:
#         raise PostNotFound()
#
#     return post
from typing import Mapping

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from ..dependencies import get_db
from . import service
from .schemas import Level


class LevelNotFound(Exception):
    pass


def existing_level_parent(level: Level, db: Session = Depends(get_db)) -> Level:
    if not level.parent:
        return level
    _level = service.get_level_by_name(name=level.parent, db=db)
    if not _level:
        raise HTTPException(status_code=404, detail=f"Parent Level {level.parent} not found")
    return level


def level_doesnt_exist_but_parent_exist(level: Level = Depends(existing_level_parent),
                                        db: Session = Depends(get_db)) -> Level:
    _level = service.get_level_by_name(name=level.name, db=db)
    if _level:
        raise HTTPException(status_code=400, detail=f"Level {level.name} already exists")
    return level


def valid_level_create(level: Level = Depends(level_doesnt_exist_but_parent_exist)) -> Level:
    return level
