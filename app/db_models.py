from datetime import datetime, timezone
from uuid import UUID, uuid4

from sqlalchemy import DateTime, String, Uuid
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base

class ReleaseRecord(Base):
    __tablename__ = "releases"

    id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )

    version: Mapped[str] = mapped_column(
        String(length=50),
        nullable=False,
    )

    environment: Mapped[str] = mapped_column(
        String(length=20),
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(length=20),
        nullable=False,
    )

    commit_sha: Mapped[str] = mapped_column(
        String(length=40),
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
    )