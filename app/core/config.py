from pydantic_settings import BaseSettings
from sqlalchemy import false #SettingsConfigDict


class Config(BaseSettings):
    # model_config = SettingsConfigDict(
    #     env_file=".env",
    #     env_file_encoding="utf-8"
    # )

    app_name: str = "My Application"
    debug_mode: bool = False
    database_url: str


class Settings(Config):
    secret_key: str
    max_connections: int
    class Config:
        env_file=".env",  # No prefix, read variables as they are
        env_file_encoding="utf-8"
        case_sensitive = False

settings = Settings()
