from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas, models
from app.database import get_db

router = APIRouter(prefix="/history", tags=["history"])


@router.get("/", response_model=list[schemas.WeatherResponse])
def get_history(db: Session = Depends(get_db)):
    logs = crud.get_last_five_requests(db)

    history_response = []
    for log in logs:
        city_name = (
            db.query(models.City).filter(models.City.id == log.city_id).first().name
        )
        history_response.append(
            {
                "city_id": log.city_id,
                "weather_summary": log.weather_summary,
                "timestamp": log.timestamp,
                "status": log.status,
            }
        )

    return history_response
