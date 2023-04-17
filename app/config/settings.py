import os

class DataBaseConfig:
    DB_USER = 'postgres' 
    DB_PASSWORD = 'postgres' 
    DB_HOST = 'db' 
    DB_PORT = '5432' 
    DB_NAME = 'postgres' 
    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Config(DataBaseConfig):
    DEBUG = False
    TESTING = False
    SECRET_KEY = ${SECRET_KEY}

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True