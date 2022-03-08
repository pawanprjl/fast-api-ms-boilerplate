from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from app.config import settings

engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URL, connect_args=settings.DATABASE_CONNECT_DICT
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
