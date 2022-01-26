import os
from dotenv import load_dotenv

load_dotenv()

class BaseConfig(object):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('BLOG_API_URI')

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    FLASK_ENV = 'development'
    SECRET_KEY = os.getenv('BBS_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class TestingConfig(BaseConfig):
    DEBUG = True

class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "production_database_uri"