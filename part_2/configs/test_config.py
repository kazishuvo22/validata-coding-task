from app_config import AppConfig

class TestConfig(AppConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"  # In-memory DB for testing
    SQLALCHEMY_TRACK_MODIFICATIONS = False