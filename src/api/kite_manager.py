from kiteconnect import KiteConnect
from src.utils.config import Config

class KiteManager:
    def __init__(self):
        self.api_key = Config.KITE_API_KEY
        self.api_secret = Config.KITE_API_SECRET
        self.access_token = Config.KITE_ACCESS_TOKEN
        self.mock_mode = Config.is_mock_mode()

        if not self.mock_mode:
            self.kite = KiteConnect(api_key=self.api_key)
            self.kite.set_access_token(self.access_token)
        else:
            self.kite = None
            print("Running in MOCK_MODE")

    def get_positions(self):
        """
        Fetch current positions. Returns mock data if in mock mode.
        """
        if self.mock_mode:
            return self._get_mock_positions()

        try:
            return self.kite.positions()
        except Exception as e:
            print(f"Error fetching positions: {e}")
            return {"day": [], "net": []}

    def _get_mock_positions(self):
        """
        Returns sample position data for testing.
        """
        return {
            "day": [],
            "net": [
                {
                    "tradingsymbol": "SBIN",
                    "exchange": "NSE",
                    "instrument_token": 779521,
                    "product": "MIS",
                    "quantity": 100,
                    "overnight_quantity": 0,
                    "multiplier": 1,
                    "average_price": 550.5,
                    "close_price": 560.0,
                    "last_price": 565.2,
                    "value": -55050.0,
                    "pnl": 1470.0,
                    "m2m": 1470.0,
                    "unrealised": 1470.0,
                    "realised": 0.0
                },
                {
                    "tradingsymbol": "RELIANCE",
                    "exchange": "NSE",
                    "instrument_token": 738561,
                    "product": "NRML",
                    "quantity": 50,
                    "overnight_quantity": 50,
                    "multiplier": 1,
                    "average_price": 2450.0,
                    "close_price": 2400.0,
                    "last_price": 2380.0,
                    "value": 0.0,
                    "pnl": -3500.0,
                    "m2m": -1000.0,
                    "unrealised": -3500.0,
                    "realised": 0.0
                },
                {
                    "tradingsymbol": "INFY",
                    "exchange": "NSE",
                    "instrument_token": 408065,
                    "product": "MIS",
                    "quantity": 0,
                    "overnight_quantity": 0,
                    "multiplier": 1,
                    "average_price": 1500.0,
                    "close_price": 1510.0,
                    "last_price": 1520.0,
                    "value": 2000.0,
                    "pnl": 2000.0,
                    "m2m": 0.0,
                    "unrealised": 0.0,
                    "realised": 2000.0
                },
                {
                    "tradingsymbol": "NIFTY23OCT19500CE",
                    "exchange": "NFO",
                    "instrument_token": 123456,
                    "product": "NRML",
                    "quantity": 50,
                    "overnight_quantity": 50,
                    "multiplier": 1,
                    "average_price": 120.0,
                    "close_price": 100.0,
                    "last_price": 85.0,
                    "value": 0.0,
                    "pnl": -1750.0,
                    "m2m": -750.0,
                    "unrealised": -1750.0,
                    "realised": 0.0
                }
            ]
        }
