from sqlalchemy import Column, String, DateTime, JSON
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from uuid import uuid4
from app.db.base import Base


class User(Base):
    # Database table name for storing application-level user data
    __tablename__ = "users"

    # Internal primary key used by the application
    # UUID is preferred for security and easier merging across systems
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    # Email and username are optional because authentication is handled
    # via external OAuth provider (Google).
    #
    # We should NOT assume email/username are always present or verified
    # at signup time, especially for social login flows.
    email = Column(String, unique=True, nullable=True)
    username = Column(String, unique=True, nullable=True)

    # OAuth tokens obtained from Google authentication flow.
    #
    # IMPORTANT:
    # These tokens are used only if the backend needs to call Google APIs
    # on behalf of the user (e.g. fetch profile, access Google services).
    #
    # If tokens are not required after login, these fields should be removed
    # to reduce security risk.
    refresh_token = Column(String, nullable=True)
    access_token = Column(String, nullable=True)

    # Expiration timestamp for the access token.
    # Storing the absolute expiry time makes validation easier
    # than storing duration (seconds).
    expires_in = Column(DateTime, nullable=True)

    # Subscription tier controls feature limits and usage policies.
    #
    # Example:
    # - free      → limited requests per day
    # - premium   → unlimited or higher quota
    #
    # String is used instead of Enum to allow future expansion
    # without database enum migrations.
    subscription_tier = Column(String, default="free")

    # Flexible JSON field for user-specific preferences.
    # If user has subscription plan then we can allow more settings.
    # Used for values that change frequently or vary per user, such as:
    # - preferred language
    # - default voice settings
    # - UI preferences
    #
    # JSON avoids frequent schema migrations for preference changes.
    settings = Column(JSON, default=dict)

    # Timestamp when the user record was created.
    # Stored in UTC to avoid timezone-related issues.
    created_at = Column(DateTime, default=datetime.utcnow)
