from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    app_name: str = "New Api"
    api_v1_prefix: str = "/api/v1"
    db_url: str = "sqlite+aiosqlite:///./db.sqlite3"
    db_echo: bool = False

    class Config:
        env_file = ".env"


settings = Settings()
