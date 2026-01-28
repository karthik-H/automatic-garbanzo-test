import os
from dotenv import load_dotenv

class Config:
    """Configuration loader for environment variables."""

    def __init__(self, env_file: str = ".env"):
        load_dotenv(env_file)
        self.api_base_url = os.getenv("API_BASE_URL")
        if not self.api_base_url:
            raise ValueError("API_BASE_URL is not set in the environment variables.")

config = Config()