import logging
from kiteconnect import KiteConnect
from src.utils.config import Config

logger = logging.getLogger(__name__)

class KiteManager:
    def __init__(self):
        self.mock_mode = Config.MOCK_MODE
        if not self.mock_mode:
            Config.validate()
            self.kite = KiteConnect(api_key=Config.KITE_API_KEY)
            self.kite.set_access_token(Config.KITE_ACCESS_TOKEN)
        else:
            logger.info("KiteManager initialized in MOCK MODE")
            self.kite = None

    def get_positions(self):
        """Fetches current positions."""
        if self.mock_mode:
            return self._get_mock_positions()
        try:
            return self.kite.positions()
        except Exception as e:
            logger.error(f"Error fetching positions: {e}")
            raise

    def _get_mock_positions(self):
        """Returns mock position data for testing."""
        return {
            "net": [
                {
                    "tradingsymbol": "SBIN",
                    "exchange": "NSE",
                    "instrument_token": 12345,
                    "product": "CNC",
                    "quantity": 100,
                    "overnight_quantity": 100,
                    "multiplier": 1,
                    "average_price": 500.0,
                    "last_price": 520.0,
                    "pnl": 2000.0,
                    "m2m": 2000.0,
                    "unrealised": 2000.0,
                    "realised": 0.0,
                    "buy_quantity": 100,
                    "buy_price": 500.0,
                    "buy_value": 50000.0,
                    "sell_quantity": 0,
                    "sell_price": 0.0,
                    "sell_value": 0.0,
                },
                {
                    "tradingsymbol": "INFY",
                    "exchange": "NSE",
                    "instrument_token": 67890,
                    "product": "CNC",
                    "quantity": 50,
                    "overnight_quantity": 50,
                    "multiplier": 1,
                    "average_price": 1500.0,
                    "last_price": 1450.0,
                    "pnl": -2500.0,
                    "m2m": -2500.0,
                    "unrealised": -2500.0,
                    "realised": 0.0,
                    "buy_quantity": 50,
                    "buy_price": 1500.0,
                    "buy_value": 75000.0,
                    "sell_quantity": 0,
                    "sell_price": 0.0,
                    "sell_value": 0.0,
                },
                {
                    "tradingsymbol": "RELIANCE",
                    "exchange": "NSE",
                    "instrument_token": 11223,
                    "product": "MIS",
                    "quantity": 10,
                    "overnight_quantity": 0,
                    "multiplier": 1,
                    "average_price": 2400.0,
                    "last_price": 2450.0,
                    "pnl": 500.0,
                    "m2m": 500.0,
                    "unrealised": 500.0,
                    "realised": 0.0,
                    "buy_quantity": 10,
                    "buy_price": 2400.0,
                    "buy_value": 24000.0,
                    "sell_quantity": 0,
                    "sell_price": 0.0,
                    "sell_value": 0.0,
                }
            ],
            "day": []
        }
