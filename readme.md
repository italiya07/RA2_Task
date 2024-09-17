## Weather API

This project is a simple weather API built using FastAPI, which fetches weather information from a third-party weather service and allows users to retrieve weather data for cities from a preset list in the database. It also logs requests and provides a history of the most recent successful requests.

### Features

- Fetch current weather for a city based on its ID.
- Log the request with a timestamp, city, and response status.
- View a history of the 5 most recent successful weather requests.

---

### Prerequisites

- Python 3.10 or higher
- SQLite (used as the database in this project)
- `pip` (Python package installer)

---

### Setup Instructions

#### 1. Clone the Repository

```bash
git clone <repository-url>
cd <repository-directory>
```

#### 2. Install Dependencies

Make sure you have Python 3.10+ installed, and then install the project dependencies:

```bash
pip install -r requirements.txt
```

#### 3. Set Up the Database

The application uses SQLite as the database, and a list of preset cities needs to be populated in the database. To do this, run the `populate_Script.py` to populate the data:

```bash
python scripts/populate_Script.py
```

This script populates a table with predefined cities like Toronto, Vancouver, Montreal, etc.

#### 4. Set Environment Variables

To use a third-party weather API like OpenWeatherMap, you need an API key. Set the following environment variable in .env:

```bash
OPENWEATHER_API_KEY=<your_api_key>
```

Make sure to replace `<your_api_key>` with your actual API key.

#### 5. Run the Application

You can run the FastAPI server locally using `uvicorn`:

```bash
uvicorn app.main:app --reload
```

The API will be accessible at `http://127.0.0.1:8000`.

---

### Endpoints

#### 1. Get Weather for a City

```http
POST /weather/
```

- **Description**: Fetches the current weather for a city based on its ID.
- **Request Body**:
  ```json
  {
    "city_id": 1
  }
  ```
- **Response**:
  - Status code: `200 OK`
  - Example Response Body:
    ```json
    {
      "city_id": 1,
      "weather_summary": "clear sky",
      "timestamp": "2024-09-10T12:00:00",
      "status": "success"
    }
    ```

#### 2. Get History of Weather Requests

```http
GET /history/
```

- **Description**: Fetches the history of the 5 most recent successful weather requests.
- **Response**:
  - Status code: `200 OK`
  - Example Response Body:
    ```json
    [
      {
        "city_id": 1,
        "weather_summary": "clear sky",
        "timestamp": "2024-09-10T12:00:00",
        "status": "success"
      },
      {
        "city_id": 2,
        "weather_summary": "cloudy",
        "timestamp": "2024-09-10T13:00:00",
        "status": "success"
      }
    ]
    ```

---

### Running Tests

Tests are included to validate the functionality of the API.

#### 1. Install `pytest` (if not already installed)

```bash
pip install pytest
```

#### 2. Run Tests

To run the test suite, use the following command:

```bash
pytest
```

This will run all tests, including those for fetching weather data and viewing the request history.

---

### Improvements and Future Enhancements

- **User Authentication**: Add OAuth or JWT-based authentication for secure access to the API.
- **Caching**: Implement caching mechanisms (e.g., Redis) to store frequently requested weather data and reduce API calls to the third-party service.
- **Error Handling**: More robust error handling for edge cases like invalid API keys, third-party API timeouts, etc.
- **Rate Limiting**: Add rate limiting to prevent abuse of the API.
- **Pagination in History Endpoint**: Add pagination support for the history of requests.

---

### Docker (Optional)

To make deployment easier, you can use the provided `Dockerfile` to containerize the application.

#### 1. Build Docker Image

```bash
docker build -t weather-api .
```

#### 2. Run Docker Container

```bash
docker run -d -p 8000:8000 weather-api
```

The API will be available at `http://localhost:8000`.
