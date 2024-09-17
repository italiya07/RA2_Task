from app.database import SessionLocal, engine
from app.models import City
from app.database import Base

Base.metadata.create_all(bind=engine)


def populate_cities():
    db = SessionLocal()
    city_names = [
        "Toronto",
        "Vancouver",
        "Montreal",
        "Calgary",
        "Ottawa",
    ]
    for city_name in city_names:
        if not db.query(City).filter(City.name == city_name).first():
            new_city = City(name=city_name)
            db.add(new_city)
    db.commit()
    db.close()


if __name__ == "__main__":
    populate_cities()
    print("Cities have been populated in the database.")
