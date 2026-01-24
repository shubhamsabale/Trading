import logging
from kiteconnect import KiteConnect
from src.utils import config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class KiteManager:
    def __init__(self):
        self.mock_mode = config.MOCK_MODE
        if not self.mock_mode:
            try:
                self.kite = KiteConnect(api_key=config.KITE_API_KEY)
                self.kite.set_access_token(config.KITE_ACCESS_TOKEN)
                logger.info("Kite Session Initialized")
            except Exception as e:
                logger.error(f"Failed to initialize Kite: {e}")
                self.mock_mode = True
                logger.info("Switching to Mock Mode")

        if self.mock_mode:
            logger.info("Kite Manager running in MOCK MODE")

    def get_positions(self):
        if self.mock_mode:
            return self._get_mock_positions()
        try:
            return self.kite.positions()
        except Exception as e:
            logger.error(f"Error fetching positions: {e}")
            return {"net": [], "day": []}

    def _get_mock_positions(self):
        # Sample mock data
        return {
            "net": [
                {
                    "tradingsymbol": "INFY",
                    "exchange": "NSE",
                    "instrument_token": 1234,
                    "quantity": 10,
                    "average_price": 1500.0,
                    "last_price": 1550.0,
                    "pnl": 500.0,
                    "m2m": 500.0
                },
                {
                    "tradingsymbol": "RELIANCE",
                    "exchange": "NSE",
                    "instrument_token": 5678,
                    "quantity": 5,
                    "average_price": 2400.0,
                    "last_price": 2350.0,
                    "pnl": -250.0,
                    "m2m": -250.0
                },
                {
                    "tradingsymbol": "TCS",
                    "exchange": "NSE",
                    "instrument_token": 9012,
                    "quantity": 20,
                    "average_price": 3200.0,
                    "last_price": 3210.0,
                    "pnl": 200.0,
                    "m2m": 200.0
                }
            ],
            "day": []
        }
