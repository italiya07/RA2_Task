from pydantic import BaseModel
from datetime import datetime


class CityBase(BaseModel):
    name: str


class CityCreate(CityBase):
    pass


class City(CityBase):
    id: int

    class Config:
        orm_mode = True


class WeatherResponse(BaseModel):
    city_id: int
    weather_summary: str
    timestamp: datetime
    status: str


class WeatherRequest(BaseModel):
    city_id: int
