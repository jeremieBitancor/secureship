from datetime import datetime, timezone
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException, status
from app.models import Release, ReleaseCreate

app = FastAPI(
    title="Secureship API",
    description="Release tracking API for the Secureship project",
    version="0.1.0",
)

releases: list[Release] = []

@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/version")
def get_version():
    return {"version": "0.1.0"}

@app.post(
    "/releases",
    response_model=Release,
    status_code=status.HTTP_201_CREATED
)

def create_release(release_data: ReleaseCreate):
    release = Release(
        id=uuid4(),
        created_at=datetime.now(timezone.utc),
        **release_data.model_dump(),
    )

    releases.append(release)

    return release

@app.get("/releases", response_model=list[Release])
def get_releases():
    return releases

@app.get("/releases/{release_id}", response_model=Release)
def get_release(release_id: UUID):
    for release in releases:
        if release.id == release_id:
            return release

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Release not found"
    )
