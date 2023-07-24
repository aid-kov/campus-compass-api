from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship

from app.db import database


class Campus(database.Base):
    __tablename__ = "campuses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    internal_name = Column(String, unique=True)

    buildings = relationship("Building", back_populates="campus")


class Building(database.Base):
    __tablename__ = "buildings"

    id = Column(Integer, primary_key=True, index=True)
    campus_id = Column(Integer, ForeignKey("campuses.id"))
    name = Column(String)
    internal_name = Column(String, unique=True)

    campus = relationship("Campus", back_populates="buildings")
    features = relationship("Feature", back_populates="building")


class Feature(database.Base):
    __tablename__ = "features"

    id = Column(Integer, primary_key=True, index=True)
    building_id = Column(Integer, ForeignKey("buildings.id"))
    name = Column(String)
    type = Column(Enum('classroom', 'bathroom', 'stairs', 'elevator', name="type", create_type=False))

    building = relationship("Building", back_populates="features")
