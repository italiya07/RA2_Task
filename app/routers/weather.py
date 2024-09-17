from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas, utils
from app.database import get_db

router = APIRouter(prefix="/weather", tags=["weather"])


@router.post("/", response_model=schemas.WeatherResponse)
def get_weather(city_request: schemas.WeatherRequest, db: Session = Depends(get_db)):
    city = crud.get_city_by_id(db, city_request.city_id)

    if not city:
        raise HTTPException(status_code=404, detail="City not found")

    weather_data = utils.fetch_weather_data(city.name)

    if weather_data is None:
        crud.log_weather_request(db, city.id, "failure", "Failed to fetch weather data")
        raise HTTPException(status_code=502, detail="Failed to fetch weather data")

    crud.log_weather_request(db, city.id, "success", weather_data["summary"])

    return {
        "city_id": city.id,
        "weather_summary": weather_data["summary"],
        "timestamp": weather_data["timestamp"],
        "status": "success",
    }
