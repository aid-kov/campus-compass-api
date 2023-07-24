from sqlalchemy.orm import Session

from app.db import models


def get_campuses(db: Session):
    return db.query(models.Campus).all()


def get_campus_buildings(db: Session, campus: str):
    campus = db.query(models.Campus).filter(models.Campus.internal_name == campus).first()
    return db.query(models.Building).filter(models.Building.campus_id == campus.id).all()


def get_building_features(db: Session, building: str):
    building = db.query(models.Building).filter(models.Building.internal_name == building).first()
    return db.query(models.Feature).filter(models.Feature.building_id == building.id).all()
