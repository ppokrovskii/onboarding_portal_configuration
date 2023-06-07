from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref

from ..database import Base

parameters_features_table = Table('parameters_features', Base.metadata,
                                  Column('parameters_col_code', String, ForeignKey('parameters.col_code')),
                                  Column('feature_name', String, ForeignKey('features.name'))
                                  )


class Parameter(Base):
    __tablename__ = "parameters"
    col_code = Column(String, primary_key=True)
    name = Column(String)
    level_name = Column(String, ForeignKey('levels.name'))
    level = relationship("Level", backref=backref("parameters", cascade="all, delete-orphan"))
    features = relationship("Feature", secondary=parameters_features_table, backref="parameters")
