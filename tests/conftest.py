import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, engine, SessionLocal
from sqlalchemy.orm import sessionmaker


# Create a test client for FastAPI
@pytest.fixture(scope="module")
def test_client():
    Base.metadata.create_all(bind=engine)
    client = TestClient(app)
    yield client
    # Base.metadata.drop_all(bind=engine)


# Session for interacting with the test database
@pytest.fixture(scope="module")
def db_session():
    connection = engine.connect()
    transaction = connection.begin()
    session = SessionLocal(bind=connection)

    yield session

    session.close()
    transaction.rollback()
    connection.close()
