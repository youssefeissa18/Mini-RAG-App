from pydantic_settings import BaseSettings, settingsconfigDict

class Settings(BaseSettings):
    
    OPENAI_API_KEY: str
    app_name: str
    app_version: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True

def get_settings():
    return Settings()