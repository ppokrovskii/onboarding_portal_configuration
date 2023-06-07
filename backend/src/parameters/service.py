from .models import Parameter
from .schemas import ParameterCreate
from ..levels import service as levels_service
from ..features import service as features_service


def get_parameters(db):
    return db.query(Parameter).all()


def get_parameter_by_name(db, name):
    return db.query(Parameter).filter(Parameter.name == name).first()


def create_parameter(db, parameter: ParameterCreate):
    level = levels_service.get_level_by_name(db, name=parameter.level)
    features = [features_service.get_feature_by_name(db, name=feature_name) for feature_name in parameter.features]
    db_parameter = Parameter(
        name=parameter.name,
        col_code=parameter.col_code,
        level_name=level.name,
        features=features,
    )
    db.add(db_parameter)
    db.commit()
    db.refresh(db_parameter)
    return db_parameter


def get_parameter_by_col_code(db, col_code):
    return db.query(Parameter).filter(Parameter.col_code == col_code).first()
