from sqlalchemy import create_engine, Column, Integer, Text, DateTime, func
from sqlalchemy.orm import sessionmaker, declarative_base
import os

Base = declarative_base()

class Greeting(Base):
  __tablename__ = 'greetings'
  id = Column(Integer, primary_key=True, autoincrement=True)
  message = Column(Text, nullable=False)
  created_at = Column(DateTime, server_default=func.now(), nullable=False)

# Try DATABASE_URL first (backwards compatibility)
DATABASE_URL = os.getenv("DATABASE_URL")

# If not provided, build from individual env vars
if DATABASE_URL is None:
  postgres_host = os.getenv("POSTGRES_HOST")
  postgres_port = os.getenv("POSTGRES_PORT", "5432")
  postgres_user = os.getenv("POSTGRES_USER")
  postgres_password = os.getenv("POSTGRES_PASSWORD")
  postgres_db = os.getenv("POSTGRES_DATABASE")

  if not all([postgres_host, postgres_user, postgres_password, postgres_db]):
    raise EnvironmentError("Either DATABASE_URL or all POSTGRES_* environment variables must be set")

  DATABASE_URL = f"postgresql://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_db}"

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine)

def init_db():
  Base.metadata.create_all(bind=engine)
