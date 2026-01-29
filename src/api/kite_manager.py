from kiteconnect import KiteConnect
from src.utils.config import get_config
import logging

class KiteManager:
    def __init__(self):
        self.config = get_config()
        self.kite = None
        self.mock_mode = self.config["MOCK_MODE"]

        if not self.mock_mode:
            self._initialize_kite()
        else:
            logging.info("Initializing KiteManager in MOCK MODE")

    def _initialize_kite(self):
        try:
            self.kite = KiteConnect(api_key=self.config["KITE_API_KEY"])
            self.kite.set_access_token(self.config["KITE_ACCESS_TOKEN"])
        except Exception as e:
            logging.error(f"Error initializing Kite: {e}")
            self.mock_mode = True
            logging.info("Falling back to MOCK MODE due to initialization failure")

    def get_positions(self):
        if self.mock_mode:
            return self._get_mock_positions()

        try:
            return self.kite.positions()
        except Exception as e:
            logging.error(f"Error fetching positions: {e}")
            return {"net": [], "day": []}

    def _get_mock_positions(self):
        # Sample positions data similar to Kite API response
        return {
            "net": [
                {
                    "tradingsymbol": "RELIANCE",
                    "exchange": "NSE",
                    "quantity": 10,
                    "average_price": 2500.0,
                    "last_price": 2550.0,
                    "pnl": 500.0,
                    "m2m": 500.0
                },
                {
                    "tradingsymbol": "TCS",
                    "exchange": "NSE",
                    "quantity": 5,
                    "average_price": 3400.0,
                    "last_price": 3350.0,
                    "pnl": -250.0,
                    "m2m": -250.0
                },
                {
                    "tradingsymbol": "INFY",
                    "exchange": "NSE",
                    "quantity": 20,
                    "average_price": 1500.0,
                    "last_price": 1520.0,
                    "pnl": 400.0,
                    "m2m": 400.0
                },
                {
                    "tradingsymbol": "HDFCBANK",
                    "exchange": "NSE",
                    "quantity": 15,
                    "average_price": 1650.0,
                    "last_price": 1600.0,
                    "pnl": -750.0,
                    "m2m": -750.0
                }
            ],
            "day": []
        }
