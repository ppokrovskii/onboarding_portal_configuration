from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..dependencies import get_db
from . import service
from .dependencies import valid_feature_create
from .schemas import Feature, FeatureCreate

router = APIRouter()


@router.get("/")
def get_features(db: Session = Depends(get_db)) -> List[Feature]:
    print("get_features")
    features = service.get_features(db)
    features = features or []
    return features


@router.post("/",
             status_code=201,
             response_model_exclude_none=True,)
def create_feature(feature: FeatureCreate = Depends(valid_feature_create), db: Session = Depends(get_db)) -> Feature:
    db_feature = service.get_feature_by_name(db, feature.name)
    return service.create_feature(db, feature)


@router.get("/name/{name}", response_model=Feature, response_model_exclude_none=True)
def get_feature_by_name(name: str, db: Session = Depends(get_db)):
    feature = service.get_feature_by_name(db, name=name)
    if feature is None:
        raise HTTPException(status_code=404, detail=f"Feature {name} not found")
    return feature
