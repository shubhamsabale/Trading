import logging
from kiteconnect import KiteConnect
from src.utils.config import Config

logger = logging.getLogger(__name__)

class KiteManager:
    def __init__(self):
        self.kite = None
        if not Config.MOCK_MODE:
            self.kite = KiteConnect(api_key=Config.KITE_API_KEY)
            self.kite.set_access_token(Config.KITE_ACCESS_TOKEN)
        else:
            logger.info("Running in MOCK_MODE")

    def get_positions(self):
        if Config.MOCK_MODE:
            return self._get_mock_positions()
        try:
            return self.kite.positions()
        except Exception as e:
            logger.error(f"Error fetching positions: {e}")
            return {"net": [], "day": []}

    def _get_mock_positions(self):
        # Sample position data as returned by Kite API
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
                    "multiplier": 1
                },
                {
                    "tradingsymbol": "TCS",
                    "exchange": "NSE",
                    "quantity": 5,
                    "average_price": 3500.0,
                    "last_price": 3450.0,
                    "pnl": -250.0,
                    "m2m": -250.0,
                    "multiplier": 1
                },
                {
                    "tradingsymbol": "INFY",
                    "exchange": "NSE",
                    "quantity": 20,
                    "average_price": 1500.0,
                    "last_price": 1520.0,
                    "pnl": 400.0,
                    "m2m": 400.0,
                    "multiplier": 1
                },
                {
                    "tradingsymbol": "HDFCBANK",
                    "exchange": "NSE",
                    "quantity": 50,
                    "average_price": 1600.0,
                    "last_price": 1580.0,
                    "pnl": -1000.0,
                    "m2m": -1000.0,
                    "multiplier": 1
                }
            ],
            "day": []
        }
