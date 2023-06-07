from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from .. import levels, features
from ..dependencies import get_db
from . import service
from .schemas import ParameterCreate


def valid_parameter_create(parameter: ParameterCreate, db: Session = Depends(get_db)) -> ParameterCreate:
    # parameter doesnt exist
    _parameter = service.get_parameter_by_name(db, name=parameter.name)
    if _parameter:
        raise HTTPException(400, f"Parameter with name {parameter.name} already exists")
    # col_code doesnt exist
    _parameter = service.get_parameter_by_col_code(db, col_code=parameter.col_code)
    if _parameter:
        raise HTTPException(400, f"Parameter with col_code {parameter.col_code} already exists")
    # level exists
    _level = levels.service.get_level_by_name(db, name=parameter.level)
    if not _level:
        raise HTTPException(404, f"Level with name {parameter.level} doesnt exist")
    # all features exist
    for feature_name in parameter.features:
        _feature = features.service.get_feature_by_name(db, name=feature_name)
        if not _feature:
            raise HTTPException(404, f"Feature with name {feature_name} doesnt exist")
    return parameter
