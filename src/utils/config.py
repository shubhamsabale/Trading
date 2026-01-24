import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

KITE_API_KEY = os.getenv("KITE_API_KEY")
KITE_API_SECRET = os.getenv("KITE_API_SECRET")
KITE_ACCESS_TOKEN = os.getenv("KITE_ACCESS_TOKEN")

# MOCK_MODE defaults to True if not specified or if keys are missing
MOCK_MODE = os.getenv("MOCK_MODE", "True").lower() == "true"

if not all([KITE_API_KEY, KITE_API_SECRET, KITE_ACCESS_TOKEN]):
    MOCK_MODE = True
