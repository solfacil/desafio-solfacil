import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

mysql_username = os.getenv('MYSQL_USERNAME')
mysql_password = os.getenv('MYSQL_PASSWORD')
mysql_host = os.getenv('MYSQL_HOST')
mysql_database = os.getenv('MYSQL_DATABASE')

SQLALCHEMY_DATABASE_URL = f"mysql://{mysql_username}:{mysql_password}@{mysql_host}/{mysql_database}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
