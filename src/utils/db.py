# pyrefly: ignore [missing-import]
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from src.utils.settings import settings

Base = declarative_base()

engine = create_engine(settings.DATABASE_URL)

session = sessionmaker(bind=engine)


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()