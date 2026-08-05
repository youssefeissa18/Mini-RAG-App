from pydantic_settings import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):
    
    OPENAI_API_KEY: str
    app_name: str
    app_version: str
    FILE_ALLOWED_TYPES : list
    FILE_MAX_SIZE_MB : int
    FILE_DEFAULT_CHUNK_SIZE : int

    POSTGRESQL_HOST : str
    POSTGRESQL_PORT : int
    POSTGRESQL_USER : str
    POSTGRESQL_PASSWORD : str
    POSTGRESQL_MAIN_DATABASE : str

    #============================LLM Configurations============================#
    GENERATION_BACKEND : str
    EMBEDDING_BACKEND : str

    OPENAI_API_KEY : str = None
    OPENAI_API_URL : str = None
    COHERE_API_KEY : str = None

    GENERATION_MODEL_ID : str = None
    EMBEDDING_MODEL_ID : str = None

    GENERATION_MODEL_ID : str = None
    EMBEDDING_MODEL_ID : str = None
    EMBEDDING_MODEL_SIZE : int = None
    INPUT_DEFAULT_MAX_CHARACTERS : int = None
    GENERATION_DEFAULT_MAX_TOKENS : int = None
    GENERATION_DEFAULT_TEMPRETURE = int = None

    #============================VectorDB Configurations============================#
    VECTOR_DB_TYPE : str
    VECTOR_DB_PATH : str
    VECTOR_DB_DISTANCE_METHOD : str = None

    # ========================= Template Configs =========================
    PRIMARY_LANG : str = "ar"
    DEFAULT_LANG : str = "en"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True

def get_settings():
    return Settings()