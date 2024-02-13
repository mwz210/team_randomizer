import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class GlobalConfig(BaseSettings):  
    class Config:
        case_sensitive = True # Ensure case sensitivity for configuration variables
    
    title: str = os.environ.get("TITLE")
    version: str = "1.0.0"  
    description: str = os.environ.get("DESCRIPTION")
    api_prefix: str = os.environ.get("API_PREFIX")
    docs_url: str = "/docs"  
    redoc_url: str = "/redoc"  
    openapi_url: str = "/openapi.json"  
  
  
settings = GlobalConfig()