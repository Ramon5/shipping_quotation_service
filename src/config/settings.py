from typing import List, Optional

from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_URL: str
    ORIGINS: Optional[List[str]] = ["*"]

    model_config = ConfigDict(env_file=".env")


settings = Settings()
