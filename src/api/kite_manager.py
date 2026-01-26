from kiteconnect import KiteConnect
from src.utils.config import KITE_API_KEY, KITE_ACCESS_TOKEN, MOCK_MODE

class KiteManager:
    def __init__(self):
        if MOCK_MODE:
            self.kite = None
            print("Running in MOCK_MODE")
        else:
            self.kite = KiteConnect(api_key=KITE_API_KEY)
            self.kite.set_access_token(KITE_ACCESS_TOKEN)

    def get_positions(self):
        if MOCK_MODE:
            return {
                "net": [
                    {"tradingsymbol": "SBIN", "m2m": 500.0, "pnl": 450.0, "quantity": 10},
                    {"tradingsymbol": "RELIANCE", "m2m": -200.0, "pnl": -250.0, "quantity": 5},
                    {"tradingsymbol": "INFY", "m2m": 1200.0, "pnl": 1100.0, "quantity": 20},
                    {"tradingsymbol": "TATASTEEL", "m2m": -300.0, "pnl": -350.0, "quantity": 50},
                ]
            }
        return self.kite.positions()
