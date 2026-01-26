class User(Base):
  __tablename__ = 'users'

  id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
  clerk_user_id = Column(String, unique=True, nullable=False)

  email = Column(String, unique=True, nullable=False)
  username = Column(String, unique=True, nullable=False)

  subscription_tier = Column(String, default='free')  # e.g., free, premium
  settings = Column(JSON, default = dict)  # User-specific settings

  created_at = Column(DateTime, default=datetime.utcnow)
  