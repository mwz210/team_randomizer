import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class GlobalConfig(BaseSettings):
    class Config:
        case_sensitive = True  # Ensure case sensitivity for configuration variables

    title: str = os.environ.get("TITLE")
    version: str = "1.0.0"
    description: str = os.environ.get("DESCRIPTION")
    api_prefix: str = os.environ.get("API_PREFIX")
    docs_url: str = "/docs"
    redoc_url: str = "/redoc"
    openapi_url: str = "/openapi.json"


class PostgreSQLConfig(BaseSettings):
    class Config:
        case_sensitive = True  # Ensure case sensitivity for configuration variables

    user: str = os.environ.get("POSTGRES_USER")
    password: str = os.environ.get("POSTGRES_PASSWORD")
    database: str = os.environ.get("POSTGRES_DB")
    host: str = os.environ.get("POSTGRES_HOST")
    port: str = os.environ.get("POSTGRES_PORT")


settings = GlobalConfig()
db_settings = PostgreSQLConfig()
