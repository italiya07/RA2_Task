from fastapi import FastAPI
from app.database import init_db, SessionLocal
from app.routers import weather, history
from app.models import City

app = FastAPI()

app.include_router(weather.router)
app.include_router(history.router)


@app.on_event("startup")
def startup_event():
    init_db()
