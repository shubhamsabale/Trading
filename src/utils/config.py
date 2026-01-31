import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    KITE_API_KEY = os.getenv("KITE_API_KEY")
    KITE_API_SECRET = os.getenv("KITE_API_SECRET")
    KITE_ACCESS_TOKEN = os.getenv("KITE_ACCESS_TOKEN")

    # Mock mode is enabled if API credentials are not provided
    MOCK_MODE = os.getenv("MOCK_MODE", "True").lower() == "true" or not (KITE_API_KEY and KITE_API_SECRET)

    MTM_DASHBOARD_PATH = "mtm_dashboard.png"
