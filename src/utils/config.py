import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    KITE_API_KEY = os.getenv("KITE_API_KEY")
    KITE_API_SECRET = os.getenv("KITE_API_SECRET")
    KITE_ACCESS_TOKEN = os.getenv("KITE_ACCESS_TOKEN")

    # Mock mode flag
    MOCK_MODE = os.getenv("MOCK_MODE", "True").lower() == "true"

    @classmethod
    def validate(cls):
        """Validates that necessary configuration is present if not in mock mode."""
        if not cls.MOCK_MODE:
            if not all([cls.KITE_API_KEY, cls.KITE_API_SECRET, cls.KITE_ACCESS_TOKEN]):
                raise ValueError("Missing Kite API configuration in .env file. "
                                 "Please set KITE_API_KEY, KITE_API_SECRET, and KITE_ACCESS_TOKEN "
                                 "or set MOCK_MODE=True.")
