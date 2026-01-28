import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    KITE_API_KEY = os.getenv("KITE_API_KEY")
    KITE_API_SECRET = os.getenv("KITE_API_SECRET")
    KITE_ACCESS_TOKEN = os.getenv("KITE_ACCESS_TOKEN")

    # Default to Mock Mode if credentials are missing
    MOCK_MODE = os.getenv("MOCK_MODE", "True").lower() in ("true", "1", "t")

    @classmethod
    def is_mock_mode(cls):
        if not all([cls.KITE_API_KEY, cls.KITE_API_SECRET, cls.KITE_ACCESS_TOKEN]):
            return True
        return cls.MOCK_MODE
