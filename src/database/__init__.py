import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

db_user = os.getenv("SK_DB_USER")
db_pass = os.getenv("SK_DB_PASS")
db_host = os.getenv("SK_DB_ENDPOINT")
db_name = os.getenv("SK_DB_NAME")

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://{}:{}@{}/{}".format(
    db_user,
    db_pass,
    db_host,
    db_name,
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():  # pragma: no cover
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
