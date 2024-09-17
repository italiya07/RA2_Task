import pytest


@pytest.mark.order(1)
def test_get_weather_valid_city(test_client):
    response = test_client.post("/weather/", json={"city_id": 1})  # Toronto

    print(response, response.json())

    assert response.status_code == 200
    data = response.json()
    assert data["city_id"] == 1
    assert "weather_summary" in data
    assert data["status"] == "success"


@pytest.mark.order(2)
def test_get_weather_invalid_city(test_client):
    response = test_client.post("/weather/", json={"city_id": 999})

    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "City not found"


@pytest.mark.order(3)
def test_get_weather_history(test_client):
    response = test_client.get("/history/")

    assert response.status_code == 200
    data = response.json()

    print(data)
    assert len(data) > 0
    assert "city_id" in data[0]
    assert "weather_summary" in data[0]
    assert "timestamp" in data[0]
    assert data[0]["status"] == "success"
