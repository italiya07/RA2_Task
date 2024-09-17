from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base


class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)


class WeatherLog(Base):
    __tablename__ = "weather_logs"

    id = Column(Integer, primary_key=True, index=True)
    city_id = Column(Integer, index=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    status = Column(String)
    weather_summary = Column(String)
