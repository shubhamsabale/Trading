from kiteconnect import KiteConnect
from src.utils.config import KITE_API_KEY, KITE_ACCESS_TOKEN, MOCK_MODE

class KiteManager:
    def __init__(self):
        if MOCK_MODE:
            self.kite = None
            print("KiteManager initialized in MOCK_MODE")
        else:
            self.kite = KiteConnect(api_key=KITE_API_KEY)
            self.kite.set_access_token(KITE_ACCESS_TOKEN)

    def get_positions(self):
        if MOCK_MODE:
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
                    "tradingsymbol": "RELIANCE",
                    "exchange": "NSE",
                    "quantity": 10,
                    "average_price": 2500.0,
                    "last_price": 2550.0,
                    "pnl": 500.0,
                    "m2m": 500.0,
                    "instrument_token": 738561
                },
                {
                    "tradingsymbol": "TCS",
                    "exchange": "NSE",
                    "quantity": 5,
                    "average_price": 3400.0,
                    "last_price": 3380.0,
                    "pnl": -100.0,
                    "m2m": -100.0,
                    "instrument_token": 2953217
                },
                {
                    "tradingsymbol": "INFY",
                    "exchange": "NSE",
                    "quantity": 20,
                    "average_price": 1500.0,
                    "last_price": 1520.0,
                    "pnl": 400.0,
                    "m2m": 400.0,
                    "instrument_token": 408065
                }
            ],
            "day": []
        }
