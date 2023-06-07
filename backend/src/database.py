import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.pool import StaticPool

DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///./onboarding_portal_configuration.db")

# database = databases.Database(DATABASE_URL)
static_pool = StaticPool if os.environ.get("static_pool") == "true" else None

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},  # https://fastapi.tiangolo.com/tutorial/sql-databases/
    poolclass=static_pool,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
