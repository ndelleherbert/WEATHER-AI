import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

settings = Settings()