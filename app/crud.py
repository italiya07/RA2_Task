from sqlalchemy.orm import Session
from app import models, schemas


def get_city_by_id(db: Session, city_id: int):
    return db.query(models.City).filter(models.City.id == city_id).first()


def log_weather_request(db: Session, city_id: int, status: str, summary: str):
    weather_log = models.WeatherLog(
        city_id=city_id, status=status, weather_summary=summary
    )
    db.add(weather_log)
    db.commit()


def get_last_five_requests(db: Session):
    return (
        db.query(models.WeatherLog)
        .filter(models.WeatherLog.status == "success")
        .order_by(models.WeatherLog.timestamp.desc())
        .limit(5)
        .all()
    )
