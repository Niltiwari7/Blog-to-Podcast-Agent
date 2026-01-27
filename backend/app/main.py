from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.db.session import engine
from app.db.base import Base

# Import models to register them with SQLAlchemy
from app.models import User, Podcast, ProcessingJob

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    debug=settings.DEBUG
)

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure properly in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    """Run on application startup"""
    # Create tables if they don't exist (for development)
    # In production, use Alembic migrations
    pass


@app.on_event("shutdown")
async def shutdown_event():
    """Run on application shutdown"""
    pass


@app.get('/')
def health_check():
    return {
        'status': 'ok',
        'service': settings.PROJECT_NAME,
        'version': settings.VERSION
    }


@app.get('/health')
def detailed_health_check():
    return {
        'status': 'healthy',
        'service': settings.PROJECT_NAME,
        'version': settings.VERSION,
        'database': 'connected'
    }
