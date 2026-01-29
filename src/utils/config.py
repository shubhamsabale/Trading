import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Kite API Configuration
KITE_API_KEY = os.getenv("KITE_API_KEY")
KITE_API_SECRET = os.getenv("KITE_API_SECRET")
KITE_ACCESS_TOKEN = os.getenv("KITE_ACCESS_TOKEN")

# Application Settings
# Default to MOCK_MODE if credentials are missing
MOCK_MODE = os.getenv("MOCK_MODE", "True").lower() == "true"

if not all([KITE_API_KEY, KITE_API_SECRET, KITE_ACCESS_TOKEN]):
    MOCK_MODE = True

def get_config():
    return {
        "KITE_API_KEY": KITE_API_KEY,
        "KITE_API_SECRET": KITE_API_SECRET,
        "KITE_ACCESS_TOKEN": KITE_ACCESS_TOKEN,
        "MOCK_MODE": MOCK_MODE
    }
