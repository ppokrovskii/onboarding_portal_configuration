from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from .dependencies import get_db
from . import service
from .dependencies import valid_level_create
from .schemas import Level, LevelCreate

router = APIRouter()


@router.get("/", response_model=List[Level], response_model_exclude_none=True)
def get_levels(db: Session = Depends(get_db)):
    levels = service.get_levels(db)
    levels = levels or []
    return levels


@router.get("/name/{name}", response_model=Level, response_model_exclude_none=True)
def get_levels(name: str, db: Session = Depends(get_db)):
    level = service.get_level_by_name(db, name=name)
    if level is None:
        raise HTTPException(status_code=404, detail=f"level {name} not found")
    return level


@router.post("/", response_model=Level,
             status_code=201,
             response_model_exclude_none=True,
             )
def create_level(level: LevelCreate = Depends(valid_level_create), db: Session = Depends(get_db)) -> Level:
    return service.create_level(db, level)
