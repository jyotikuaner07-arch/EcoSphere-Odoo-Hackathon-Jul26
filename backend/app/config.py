# app/config.py
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # App Settings
    PROJECT_NAME: str = "EcoSphere ESG Management Platform"
    
    # Database Settings
    # Defaulting to the local MySQL setup discussed in progress summary
    DATABASE_URL: str = "mysql+pymysql://root:password@127.0.0.1:3306/ecosphere"
    
    # JWT Settings
    JWT_SECRET: str = "hcakathon_secret_key_change_in_production"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRE_MINUTES: int = 480  # 8 hours
    
    # CORS
    CORS_ORIGINS: str = "http://localhost:3000"
    
    # File Uploads
    UPLOAD_DIR: str = "uploads"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()