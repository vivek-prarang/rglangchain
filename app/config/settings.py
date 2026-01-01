from pydantic_settings import BaseSettings
from typing import Optional, Any

class Settings(BaseSettings):
    app_name: Optional[str] = "FastAPI"
    debug: Optional[bool] = False
    app_version: Optional[str] = "0.0.1"

    app_port : Optional[int] = 8000
    app_host : Optional[str] = "127.0.0.1"

    database_url: Optional[str] = None
    secret_key: Optional[str] = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    algorithm: Optional[str] = "HS256"
    access_token_expire_min: Optional[int] = 30


    class Config:
        env_file = ".env"
        case_sensitive = False
        extra = "allow"
settings=Settings()
