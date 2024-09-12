import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://localhost/personal_finance_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
