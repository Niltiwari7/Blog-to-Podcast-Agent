from sqlalchemy import Column, String, DateTime, Integer, ForeignKey, Enum, Text
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from uuid import uuid4
from app.db.base import Base
from app.core.enum import JobType, JobStatus


class ProcessingJob(Base):
    __tablename__ = "processing_jobs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    podcast_id = Column(UUID(as_uuid=True), ForeignKey("podcasts.id"), nullable=False)

    job_type = Column(Enum(JobType), nullable=False)
    status = Column(Enum(JobStatus), default=JobStatus.pending)

    attempt = Column(Integer, default=0)
    max_attempts = Column(Integer, default=3)

    error_message = Column(Text)
    error_code = Column(String)

    started_at = Column(DateTime)
    completed_at = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)
