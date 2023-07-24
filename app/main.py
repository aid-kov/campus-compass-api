from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from app import crud
from app.db import database, models

app = FastAPI()

models.database.Base.metadata.create_all(bind=database.engine)


# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/campus")
async def get_campuses(db: Session = Depends(get_db)):
    campuses = crud.get_campuses(db)
    if campuses is None:
        raise HTTPException(status_code=404, detail="No campuses found. Uh oh.")
    return campuses


@app.get("/buildings/{campus}")
async def get_buildings(campus: str, db: Session = Depends(get_db)):
    buildings = crud.get_campus_buildings(db, campus)
    if buildings is None:
        raise HTTPException(status_code=404, detail="No buildings found for campus")
    return buildings


@app.get("/features/{building}")
async def get_features(building: str, db: Session = Depends(get_db)):
    features = crud.get_building_features(db, building)
    if features is None:
        raise HTTPException(status_code=404, detail="No campuses found. How??")
    return features
