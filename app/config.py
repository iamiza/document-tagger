from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Document Tagger"
    DEBUG: bool = True

    class Config:
        env_file = ".env"

settings = Settings()
