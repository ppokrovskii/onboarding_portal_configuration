from typing import Optional

from pydantic import BaseModel


class FeatureBase(BaseModel):
    name: str
    parent: Optional[str] = None


class FeatureCreate(FeatureBase):
    pass


class Feature(FeatureBase):
    # id: int

    class Config:  # https://fastapi.tiangolo.com/tutorial/sql-databases/#use-pydantics-orm_mode
        orm_mode = True
