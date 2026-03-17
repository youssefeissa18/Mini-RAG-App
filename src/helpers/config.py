from pydantic_settings import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):
    
    OPENAI_API_KEY: str
    app_name: str
    app_version: str
    FILE_ALLOWED_TYPES : list
    FILE_MAX_SIZE_MB : int
    FILE_DEFAULT_CHUNK_SIZE : int


    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True

def get_settings():
    return Settings()