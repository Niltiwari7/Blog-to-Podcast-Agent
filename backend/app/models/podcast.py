from sqlalchemy import Column, String, DateTime, JSON, Integer, ForeignKey, Enum
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from uuid import uuid4
from app.db.base import Base
from app.core.enum import SourceType


class Podcast(Base):
    # table name in the database
    __tablename__ = 'podcasts'
    
    # primary key which is used to uniquely identify each podcast
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    # foreign key to the users table to associate the podcast with a user
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    
    # title and description of the podcast
    title = Column(String, nullable=False)
    description = Column(String)

   # we will support multiple source types in the future (e.g., text, URL, file upload)
    source_type = Column(Enum(SourceType), nullable=False)
    original_url = Column(String)
    source_text = Column(String) 
   
    # audio file path and duration this will come from the TTS service
    # path where the generated audio file is stored
    audio_object_key  = Column(String)
    audio_duration = Column(Integer)  # Duration in seconds
    word_count = Column(Integer)
    
    # JSON field to store various voice settings like speed, pitch, volume, etc.
    voice_settings = Column(JSON, default=dict)  # It depends on user subscription plan
    
    # timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)