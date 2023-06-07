# pydantic models
from typing import Optional

from pydantic import BaseModel


class LevelBase(BaseModel):
    name: str
    parent: Optional[str] = None
    sub_level: Optional[str] = None


class LevelCreate(LevelBase):
    pass


class Level(LevelBase):
    # id: int

    class Config:  # https://fastapi.tiangolo.com/tutorial/sql-databases/#use-pydantics-orm_mode
        orm_mode = True
