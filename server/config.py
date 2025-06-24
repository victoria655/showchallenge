import os

class Config:
    SECRET_KEY = os.environ.get("FLASK_SECRET_KEY", "fallback-secret")
    JWT_SECRET_KEY = os.environ.get("FLASK_JWT_SECRET_KEY", "fallback-jwt")
    SQLALCHEMY_DATABASE_URI = os.environ.get("FLASK_SQLALCHEMY_DATABASE_URI", "sqlite:///app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True