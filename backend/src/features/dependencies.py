from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from ..dependencies import get_db
from . import service
from .schemas import Feature


def existing_feature_parent(feature: Feature, db: Session = Depends(get_db)) -> Feature:
    if not feature.parent:
        return feature
    _feature = service.get_feature_by_name(db, feature.parent)
    if not _feature:
        raise HTTPException(status_code=404, detail=f"Parent Feature {feature.parent} not found")
    return feature


def feature_doesnt_exist_but_parent_exists(feature: Feature = Depends(existing_feature_parent),
                                           db: Session = Depends(get_db)) -> Feature:
    _feature = service.get_feature_by_name(db, feature.name)
    if _feature:
        raise HTTPException(status_code=400, detail=f"Feature {feature.name} already exists")
    return feature


def valid_feature_create(feature: Feature = Depends(feature_doesnt_exist_but_parent_exists)) -> Feature:
    return feature
