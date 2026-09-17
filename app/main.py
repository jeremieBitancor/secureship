from uuid import UUID

from fastapi import FastAPI, HTTPException, status, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.db_models import ReleaseRecord
from app.models import Release, ReleaseCreate

app = FastAPI(
    title="Secureship API"
)

@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/version")
def get_version():
    return {"version": app.version}

@app.post(
    "/releases",
    response_model=Release,
    status_code=status.HTTP_201_CREATED
)
def create_release(release_data: ReleaseCreate, db: Session = Depends(get_db),):
    release = ReleaseRecord(
        **release_data.model_dump(),
    )

    db.add(release)
    db.commit()
    db.refresh(release)

    return release

@app.get("/releases", response_model=list[Release])
def get_releases(db: Session = Depends(get_db)):
    statement = select(ReleaseRecord).order_by(ReleaseRecord.created_at.desc())
    return list(db.scalars(statement).all())

@app.get("/releases/{release_id}", response_model=Release)
def get_release(release_id: UUID, db: Session = Depends(get_db)):
    release = db.get(ReleaseRecord, release_id)

    if release is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Release not found"
        )
    return release

