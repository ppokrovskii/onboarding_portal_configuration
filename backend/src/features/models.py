# db models
from sqlalchemy import Column, String

from ..database import Base


class Feature(Base):
    __tablename__ = "features"
    name = Column(String, primary_key=True)
    parent = Column(String, nullable=True)
