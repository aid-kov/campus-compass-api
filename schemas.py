from pydantic import BaseModel


class CampusBase(BaseModel):
    name: str
    internal_name: str


# We are not doing CREATE right now, so we'll leave this out
class CampusCreate(CampusBase):
    pass


class Campus(CampusBase):
    id: int

    class Config:
        orm_mode = True


class BuildingBase(BaseModel):
    name: str
    internal_name: str


class BuildingCreate(BuildingBase):
    pass


class Building(BuildingBase):
    id: int
    campus_id: int

    class Config:
        orm_mode = True


class FeatureBase(BaseModel):
    name: str
    type: str


class FeatureCreate(FeatureBase):
    pass


class Feature(FeatureBase):
    id: int
    building_id: int

    class Config:
        orm_mode = True
