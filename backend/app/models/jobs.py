from sqlalchemy import Column, String, DateTime, Integer, ForeignKey, Enum, Text
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from uuid import uuid4
from app.db.base import Base
from app.core.enum import JobType, JobStatus


class ProcessingJob(Base):
    # table name in the database
    __tablename__ = "processing_jobs"
    
    # primary key for each processing job
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    # foreign key to the podcast table to associate the job with a podcast
    # because each job is related to a specific podcast
    podcast_id = Column(UUID(as_uuid=True), ForeignKey("podcasts.id"), nullable=False)

    # other columns related to the job
    job_type = Column(Enum(JobType), nullable=False)

    # status of the job (e.g., pending, running, success, failed)
    # It helps to track the progress of the job if fail we can again retry
    status = Column(Enum(JobStatus), default=JobStatus.pending)

    # Attempt tracking for retries
    attempt = Column(Integer, default=0)

    # Maximum number of attempts allowed
    max_attempts = Column(Integer, default=3)

    # while processing if any error occurs we can log it here
    error_message = Column(Text)
    
    # Each error we can have a specific code to identify the type of error
    error_code = Column(String)
    
    # timestamps to track job lifecycle
    started_at = Column(DateTime)
    completed_at = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)