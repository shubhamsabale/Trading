from kiteconnect import KiteConnect
from src.utils.config import KITE_API_KEY, KITE_API_SECRET, KITE_ACCESS_TOKEN, MOCK_MODE
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class KiteManager:
    def __init__(self):
        self.kite = None
        if not MOCK_MODE:
            if KITE_API_KEY:
                self.kite = KiteConnect(api_key=KITE_API_KEY)
                if KITE_ACCESS_TOKEN:
                    self.kite.set_access_token(KITE_ACCESS_TOKEN)
                    logger.info("Kite session initialized with provided access token.")
                else:
                    logger.warning("KITE_ACCESS_TOKEN missing. You may need to call generate_session.")
            else:
                logger.error("KITE_API_KEY missing. Cannot initialize KiteConnect.")
                logger.warning("Switching to MOCK_MODE.")
        else:
            logger.info("KiteManager initialized in MOCK_MODE.")

    def get_login_url(self):
        """
        Returns the login URL for Zerodha Kite.
        """
        if self.kite:
            return self.kite.login_url()
        return "https://kite.zerodha.com/connect/login?api_key=MOCK_API_KEY"

    def generate_session(self, request_token):
        """
        Generates an access token using the request token.
        """
        if not self.kite or not KITE_API_SECRET:
            logger.error("KiteConnect not initialized or KITE_API_SECRET missing.")
            return None

        try:
            data = self.kite.generate_session(request_token, api_secret=KITE_API_SECRET)
            self.kite.set_access_token(data["access_token"])
            logger.info("Session generated successfully.")
            return data
        except Exception as e:
            logger.error(f"Error generating session: {e}")
            return None

    def get_positions(self):
        if MOCK_MODE or not self.kite:
            return self._get_mock_positions()

        try:
            return self.kite.positions()
        except Exception as e:
            logger.error(f"Error fetching positions: {e}")
            return {"net": [], "day": []}

    def _get_mock_positions(self):
        # Mock data for demonstration including diverse instruments and average_price
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
                },
                {
                    "tradingsymbol": "HDFCBANK",
                    "exchange": "BSE",
                    "quantity": 200,
                    "average_price": 1450.0,
                    "last_price": 1465.0,
                    "m2m": 3000.0,
                    "pnl": 3000.0
                }
            ],
            "day": []
        }
