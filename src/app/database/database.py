from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import time


Base = declarative_base()
engine = create_engine("mysql+mysqlconnector://admin:root@mysql:3306/solfacil") #set URL in envioremnet variable


async def init_db():
    max_tries= 10
    sleep_timer = 60
    tries = 0
    
    while tries < max_tries:
        try:
            Base.metadata.create_all(bind=engine)
            return
        except Exception as e:
            print(f"Error: {e}. Retrying in {sleep_timer} seconds...")
            tries += 1
            time.sleep(sleep_timer)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)