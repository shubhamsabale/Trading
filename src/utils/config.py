import os
from dotenv import load_dotenv

load_dotenv()

KITE_API_KEY = os.getenv("KITE_API_KEY")
KITE_API_SECRET = os.getenv("KITE_API_SECRET")
KITE_ACCESS_TOKEN = os.getenv("KITE_ACCESS_TOKEN")

# Default to Mock mode if credentials are not provided
MOCK_MODE = os.getenv("MOCK_MODE", "true").lower() == "true"
