import os
from dotenv import load_dotenv

load_dotenv()

KITE_API_KEY = os.getenv("KITE_API_KEY")
KITE_API_SECRET = os.getenv("KITE_API_SECRET")
KITE_ACCESS_TOKEN = os.getenv("KITE_ACCESS_TOKEN")

MOCK_MODE = os.getenv("MOCK_MODE", "True").lower() == "true"

if not all([KITE_API_KEY, KITE_API_SECRET, KITE_ACCESS_TOKEN]) and not MOCK_MODE:
    print("Warning: Kite API credentials missing. Switching to MOCK_MODE.")
    MOCK_MODE = True
