from pydantic_settings import BaseSettings
from pydantic import BaseModel
from typing import List


class DbSettings(BaseModel):
    url: str = "sqlite+aiosqlite:///./db.sqlite3"
    echo: bool = True


class Settings(BaseSettings):
    app_name: str = "New Api"
    api_v1_prefix: str = "/api/v1"

    db: DbSettings = DbSettings()

    class Config:
        env_file = ".env"


settings = Settings()
