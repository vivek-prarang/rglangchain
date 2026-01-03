from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional, List


class Settings(BaseSettings):
    # ---------- App ----------
    app_name: str = "My Application"
    app_version: str = "0.0.1"
    debug_mode: bool = False

    app_host: str = "127.0.0.1"
    app_port: int = 8000

    # ---------- Database ----------
    database_url: str
    max_connections: int = 10

    # ---------- Security ----------
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_min: int = 30

    # ---------- API ----------
    api_version: str = "v1"
    log_level: str = "info"

    allowed_hosts: List[str] = ["localhost"]
    cors_origins: List[str] = [
        "http://localhost",
        "http://localhost:8080",
        "http://localhost:3000",
    ]

    # ---------- Pydantic Settings ----------
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )


settings = Settings()
