import os
import logging
from dotenv import load_dotenv

class Config:
  load_dotenv()
  ENV = os.getenv('ENV', 'development')
  HOST = os.getenv('Host')
  PORT=os.getenv('PORT')
  SECRET_KEY=os.getenv('SECRET_KEY')
  LOG_LEVEL=logging.DEBUG
  SQLALCHEMY_DATABASE_URI = os.environ.get('DB_CONNECTION_STRING')
  SQLALCHEMY_TRACK_MODIFICATIONS=False

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    LOG_LEVEL = logging.ERROR    