import logging
from kiteconnect import KiteConnect
from src.utils.config import Config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class KiteManager:
    def __init__(self):
        self.mock_mode = Config.MOCK_MODE
        if not self.mock_mode:
            self.kite = KiteConnect(api_key=Config.KITE_API_KEY)
            self.kite.set_access_token(Config.KITE_ACCESS_TOKEN)
            logger.info("KiteManager initialized in LIVE mode")
        else:
            self.kite = None
            logger.info("KiteManager initialized in MOCK mode")

    def get_positions(self):
        if self.mock_mode:
            return self._get_mock_positions()
        try:
            return self.kite.positions()
        except Exception as e:
            logger.error(f"Error fetching positions: {e}")
            return {"net": [], "day": []}

    def _get_mock_positions(self):
        # Sample mock data mimicking Kite API response
        return {
            "net": [
                {
                    "tradingsymbol": "SBIN",
                    "exchange": "NSE",
                    "quantity": 100,
                    "average_price": 500.0,
                    "last_price": 510.0,
                    "pnl": 1000.0,
                    "m2m": 1000.0,
                    "multiplier": 1
                },
                {
                    "tradingsymbol": "RELIANCE",
                    "exchange": "NSE",
                    "quantity": 50,
                    "average_price": 2400.0,
                    "last_price": 2380.0,
                    "pnl": -1000.0,
                    "m2m": -1000.0,
                    "multiplier": 1
                },
                {
                    "tradingsymbol": "NIFTY24FEB22000CE",
                    "exchange": "NFO",
                    "quantity": 50,
                    "average_price": 100.0,
                    "last_price": 120.0,
                    "pnl": 1000.0,
                    "m2m": 1000.0,
                    "multiplier": 1
                }
            ],
            "day": []
        }
