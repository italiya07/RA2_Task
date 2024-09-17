import requests
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def fetch_weather_data(city_name: str):
    params = {"q": city_name, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        return None

    data = response.json()
    summary = data["weather"][0]["description"]

    return {"summary": summary, "timestamp": datetime.now()}
