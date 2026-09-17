# SecureShip

SecureShip is a release-tracking API built as a hands-on Cloud and DevSecOps portfolio project. It demonstrates how a Python application can be tested, containerized, connected to PostgreSQL, and prepared for automated cloud deployment.

## Current Features

- FastAPI REST API
- Health and version endpoints
- Create and retrieve release records
- Pydantic request validation
- PostgreSQL persistence
- SQLAlchemy ORM
- Dockerized API
- Docker Compose orchestration
- PostgreSQL health checks
- Persistent database volume
- Pytest API tests from the earlier in-memory stage

> The pytest suite will be updated for isolated database testing in Stage 3.3.

## Architecture

```text
Client
  |
  v
FastAPI container :8000
  |
  v
SQLAlchemy + Psycopg
  |
  v
PostgreSQL container :5432
  |
  v
Named Docker volume
```

## Project Structure

```text
secureship/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── db_models.py
│   └── database.py
├── tests/
│   └── test_main.py
├── .dockerignore
├── .env.example
├── .gitignore
├── compose.yaml
├── Dockerfile
├── requirements.txt
└── README.md
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/health` | Check API health |
| `GET` | `/version` | Get the application version |
| `POST` | `/releases` | Create a release record |
| `GET` | `/releases` | List all releases |
| `GET` | `/releases/{release_id}` | Get a release by ID |

## Run with Docker Compose

### 1. Create the environment file

Copy the example file:

```bash
cp .env.example .env
```

Set local values in `.env`:

```dotenv
POSTGRES_USER=secureship
POSTGRES_PASSWORD=replace-with-a-local-password
POSTGRES_DB=secureship
```

Never commit `.env` or real credentials.

### 2. Build and start the stack

```bash
docker compose up --build -d
```

Check the services:

```bash
docker compose ps
```

View API logs:

```bash
docker compose logs -f api
```

### 3. Open the API

- Swagger UI: <http://127.0.0.1:8000/docs>
- Health check: <http://127.0.0.1:8000/health>

Example release request:

```json
{
  "version": "0.2.0",
  "environment": "dev",
  "status": "deployed",
  "commit_sha": "a82d910"
}
```

### 4. Stop the stack

```bash
docker compose down
```

The PostgreSQL data remains in the named volume. To delete the volume and all local database records intentionally, use:

```bash
docker compose down -v
```

## Database Inspection

Open PostgreSQL:

```bash
docker compose exec db psql -U secureship -d secureship
```

Useful commands:

```sql
\dt
\d releases
SELECT * FROM releases;
\q
```

## Local Development

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

When running the API outside Docker, PostgreSQL must already be running and `DATABASE_URL` must be configured:

```bash
export DATABASE_URL="postgresql+psycopg://secureship:your-local-password@localhost:5432/secureship"
python -m uvicorn app.main:app --reload
```

## Roadmap

- [x] Build the FastAPI release API
- [x] Add request validation
- [x] Add initial pytest coverage
- [x] Create a Docker image
- [x] Add PostgreSQL with Docker Compose
- [x] Persist releases with SQLAlchemy
- [ ] Isolate database tests and restore full pytest coverage
- [ ] Add Alembic database migrations
- [ ] Add GitHub Actions CI
- [ ] Deploy to AWS
- [ ] Provision infrastructure with Terraform
- [ ] Add DevSecOps security gates
- [ ] Add monitoring and alerts

## Current Version

SecureShip is currently in early development at version `0.2.0`.

