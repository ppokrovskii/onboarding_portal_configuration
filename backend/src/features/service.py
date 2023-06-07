from . import models


def get_features(db):
    return db.query(models.Feature).all()


def get_feature_by_name(db, name) -> models.Feature:
    return db.query(models.Feature).filter(models.Feature.name == name).first()


def create_feature(db, feature):
    db_feature = models.Feature(**feature.dict())
    db.add(db_feature)
    db.commit()
    db.refresh(db_feature)
    return db_feature
