from datetime import datetime
from typing import Literal
from uuid import UUID
from pydantic import BaseModel, Field

class ReleaseCreate(BaseModel):
    version: str = Field(min_length=1, examples=["1.0.0"])
    environment: Literal["dev", "staging", "production"]
    status: Literal["pending", "deploying", "deployed", "failed"]
    commit_sha: str = Field(min_length=7, max_length=40)

class Release(ReleaseCreate):
    id: UUID
    created_at: datetime