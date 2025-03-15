from sqlalchemy import create_engine, Column, Integer, Text, DateTime, func
from sqlalchemy.orm import sessionmaker, declarative_base
import os

Base = declarative_base()

class Greeting(Base):
  __tablename__ = 'greetings'
  id = Column(Integer, primary_key=True, autoincrement=True)
  message = Column(Text, nullable=False)
  created_at = Column(DateTime, server_default=func.now(), nullable=False)

DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL is None:
  raise EnvironmentError("DATABASE_URL environment variable not set")
engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine)

def init_db():
  Base.metadata.create_all(bind=engine)
