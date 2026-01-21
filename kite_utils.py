import os
from kiteconnect import KiteConnect
from dotenv import load_dotenv

load_dotenv()

class MockKite:
    def __init__(self):
        pass

    def positions(self):
        return {
            "net": [
                {
                    "tradingsymbol": "SBIN",
                    "exchange": "NSE",
                    "product": "CNC",
                    "quantity": 100,
                    "average_price": 600.0,
                    "last_price": 615.5,
                    "m2m": 1550.0,
                    "pnl": 1550.0
                },
                {
                    "tradingsymbol": "INFY",
                    "exchange": "NSE",
                    "product": "CNC",
                    "quantity": 50,
                    "average_price": 1500.0,
                    "last_price": 1480.0,
                    "m2m": -1000.0,
                    "pnl": -1000.0
                },
                {
                    "tradingsymbol": "RELIANCE",
                    "exchange": "NSE",
                    "product": "CNC",
                    "quantity": 20,
                    "average_price": 2500.0,
                    "last_price": 2550.0,
                    "m2m": 1000.0,
                    "pnl": 1000.0
                }
            ],
            "day": []
        }

class KiteManager:
    def __init__(self, api_key=None, api_secret=None, access_token=None, mock=False):
        self.mock = mock
        if mock:
            self.kite = MockKite()
        else:
            self.api_key = api_key or os.getenv("KITE_API_KEY")
            self.api_secret = api_secret or os.getenv("KITE_API_SECRET")
            self.access_token = access_token or os.getenv("KITE_ACCESS_TOKEN")

            if not self.api_key or not self.api_secret:
                print("Kite API credentials not found. Switching to mock mode.")
                self.mock = True
                self.kite = MockKite()
            else:
                self.kite = KiteConnect(api_key=self.api_key)
                if self.access_token:
                    self.kite.set_access_token(self.access_token)
                else:
                    print("Access token not found. You need to authenticate first.")

    def get_positions(self):
        try:
            return self.kite.positions()
        except Exception as e:
            print(f"Error fetching positions: {e}")
            return None
