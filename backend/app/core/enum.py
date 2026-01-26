from enum import Enum

class PodcastStatus(str, Enum):
  processing = 'processing'
  completed = 'completed'
  failed = 'failed'

class SourceType(str, Enum):
  url = 'url'
  text = 'text'
  makrdown = 'markdown'

class JobType(str, Enum):
    fetch_source = "fetch_source"
    clean_text = "clean_text"
    generate_audio = "generate_audio"
    upload_audio = "upload_audio"
    finalize = "finalize"


class JobStatus(str, Enum):
    pending = "pending"
    running = "running"
    success = "success"
    failed = "failed"
    retrying = "retrying"