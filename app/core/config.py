import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"
    APP_NAME: str = os.getenv("APP_NAME", "DevCalc")

settings = Settings()
