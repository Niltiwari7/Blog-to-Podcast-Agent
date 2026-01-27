from sqlalchemy import Column, String, DateTime, JSON, Integer, ForeignKey, Enum
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from uuid import uuid4
from app.db.base import Base
from app.core.enum import SourceType


class Podcast(Base):
    __tablename__ = 'podcasts'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    
    title = Column(String, nullable=False)
    description = Column(String)

    source_type = Column(Enum(SourceType), nullable=False)
    original_url = Column(String)
    source_text = Column(String) 

    audio_file_path = Column(String)
    audio_duration = Column(Integer)  # Duration in seconds
    word_count = Column(Integer)

    voice_settings = Column(JSON, default=dict)  # It depends on user subscription plan

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)