from kiteconnect import KiteConnect
from src.utils.config import KITE_API_KEY, KITE_ACCESS_TOKEN, MOCK_MODE
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class KiteManager:
    def __init__(self):
        self.kite = None
        if not MOCK_MODE:
            if KITE_API_KEY and KITE_ACCESS_TOKEN:
                self.kite = KiteConnect(api_key=KITE_API_KEY)
                self.kite.set_access_token(KITE_ACCESS_TOKEN)
                logger.info("Kite session initialized.")
            else:
                logger.warning("Kite credentials missing. Switching to MOCK_MODE.")
        else:
            logger.info("KiteManager initialized in MOCK_MODE.")

    def get_positions(self):
        if MOCK_MODE or not self.kite:
            return self._get_mock_positions()

        try:
            return self.kite.positions()
        except Exception as e:
            logger.error(f"Error fetching positions: {e}")
            return {"net": [], "day": []}

    def _get_mock_positions(self):
        # Mock data for demonstration
        return {
            "net": [
                {
                    "tradingsymbol": "SBIN",
                    "exchange": "NSE",
                    "quantity": 100,
                    "average_price": 730.50,
                    "last_price": 750.50,
                    "m2m": 1500.0,
                    "pnl": 2000.0
                },
                {
                    "tradingsymbol": "RELIANCE",
                    "exchange": "NSE",
                    "quantity": 50,
                    "average_price": 2880.00,
                    "last_price": 2900.00,
                    "m2m": -500.0,
                    "pnl": 1000.0
                },
                {
                    "tradingsymbol": "NIFTY24MAR22000CE",
                    "exchange": "NFO",
                    "quantity": 50,
                    "average_price": 70.0,
                    "last_price": 120.0,
                    "m2m": 2500.0,
                    "pnl": 2500.0
                },
                {
                    "tradingsymbol": "CRUDEOIL24MARFUT",
                    "exchange": "MCX",
                    "quantity": 100,
                    "average_price": 6512.0,
                    "last_price": 6500.0,
                    "m2m": -1200.0,
                    "pnl": -1200.0
                }
            ],
            "day": []
        }
