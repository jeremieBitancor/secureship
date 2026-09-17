# SecureShip

SecureShip is a FastAPI-based release tracking API built as a hands-on Cloud and DevSecOps portfolio project.

## Current Features

* Health check endpoint
* Application version endpoint
* Create a release
* List all releases
* Get a release by ID
* Request validation
* Automated API tests with pytest

## Project Structure

```text
secureship/
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── models.py
├── tests/
│   └── test_main.py
├── requirements.txt
└── README.md
```

## Setup

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the API:

```bash
python -m uvicorn app.main:app --reload
```

Open the API documentation:

```text
http://127.0.0.1:8000/docs
```

## Run Tests

```bash
python -m pytest -v
```

## API Endpoints

| Method | Endpoint                 | Description         |
| ------ | ------------------------ | ------------------- |
| GET    | `/health`                | Check API health    |
| GET    | `/version`               | Get API version     |
| POST   | `/releases`              | Create a release    |
| GET    | `/releases`              | List releases       |
| GET    | `/releases/{release_id}` | Get a release by ID |

## Current Limitation

Release data is stored in memory and is deleted whenever the application restarts. PostgreSQL persistence will be added in a later stage.
