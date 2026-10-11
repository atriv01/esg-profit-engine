import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Read connection string from environment or use local Docker default
DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "postgresql://esg_admin:postgres_dev_password@localhost:5432/esg_engine"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
