import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

class AppConfig:
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecret")

    DATABASE_NAME = os.getenv("DATABASE_NAME")
    SERVER_NAME = os.getenv("SERVER_NAME")
    DB_USERNAME = os.getenv("DB_USERNAME")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DRIVER = os.getenv("DRIVER")

    # Construct SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_DATABASE_URI = (
        f"mssql+pyodbc://{DB_USERNAME}:{DB_PASSWORD}@{SERVER_NAME}/{DATABASE_NAME}"
        f"?driver={DRIVER.replace(' ', '+')}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False