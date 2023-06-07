# db models
from sqlalchemy import Column, String

from ..database import Base


class Level(Base):
    __tablename__ = "levels"
    name = Column(String, primary_key=True)
    parent = Column(String, nullable=True)
    sub_level = Column(String, nullable=True)

    # items = relationship("Item", back_populates="owner")
