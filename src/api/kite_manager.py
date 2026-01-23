from kiteconnect import KiteConnect
from src.utils import config

class KiteManager:
    def __init__(self):
        self.api_key = config.KITE_API_KEY
        self.api_secret = config.KITE_API_SECRET
        self.access_token = config.KITE_ACCESS_TOKEN
        self.mock_mode = config.MOCK_MODE

        if not self.mock_mode:
            if not self.api_key:
                print("Warning: KITE_API_KEY not found in environment. Switching to MOCK_MODE.")
                self.mock_mode = True
            else:
                self.kite = KiteConnect(api_key=self.api_key)
                if self.access_token:
                    self.kite.set_access_token(self.access_token)

        if self.mock_mode:
            self.kite = None
            print("KiteManager initialized in MOCK_MODE")

    def get_positions(self):
        if self.mock_mode:
            return self._get_mock_positions()

        try:
            return self.kite.positions()
        except Exception as e:
            print(f"Error fetching positions: {e}")
            return {"net": [], "day": []}

    def _get_mock_positions(self):
        # Sample mock data for testing
        return {
            "net": [
                {
                    "tradingsymbol": "SBIN",
                    "exchange": "NSE",
                    "quantity": 100,
                    "average_price": 500.0,
                    "last_price": 515.0,
                    "instrument_token": 779521
                },
                {
                    "tradingsymbol": "INFY",
                    "exchange": "NSE",
                    "quantity": 50,
                    "average_price": 1500.0,
                    "last_price": 1480.0,
                    "instrument_token": 408065
                },
                {
                    "tradingsymbol": "RELIANCE",
                    "exchange": "NSE",
                    "quantity": 20,
                    "average_price": 2500.0,
                    "last_price": 2550.0,
                    "instrument_token": 738561
                },
                {
                    "tradingsymbol": "TATASTEEL",
                    "exchange": "NSE",
                    "quantity": 200,
                    "average_price": 110.0,
                    "last_price": 112.5,
                    "instrument_token": 895745
                }
            ],
            "day": []
        }
