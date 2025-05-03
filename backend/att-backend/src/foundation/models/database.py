from os import getenv
from typing import Generator

from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker, Session

DEFAULT_DATABASE_URL = getenv(
    "ATT_DB_URL",
    "postgresql+pg8000://secret_user:secret_password@127.0.0.1/abc123",
)


def get_engine() -> Engine:
    return create_engine(DEFAULT_DATABASE_URL)


def get_sessionmaker(engine: Engine) -> sessionmaker[Session]:
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)


engine = get_engine()
LocalSession = get_sessionmaker(engine)


def get_db() -> Generator[Session]:
    db = LocalSession()
    try:
        yield db
    finally:
        db.close_all()
