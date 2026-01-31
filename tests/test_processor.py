import unittest
import pandas as pd
from src.core.data_processor import process_positions, calculate_total_mtm

class TestDataProcessor(unittest.TestCase):
    def setUp(self):
        self.mock_data = {
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
                }
            ]
        }

    def test_process_positions(self):
        df = process_positions(self.mock_data)
        self.assertFalse(df.empty)
        self.assertEqual(len(df), 2)
        self.assertIn('m2m', df.columns)
        self.assertEqual(df.iloc[0]['tradingsymbol'], "SBIN")

    def test_calculate_total_mtm(self):
        df = process_positions(self.mock_data)
        total_mtm = calculate_total_mtm(df)
        self.assertEqual(total_mtm, 0.0)

    def test_empty_positions(self):
        df = process_positions({"net": []})
        self.assertTrue(df.empty)
        self.assertEqual(calculate_total_mtm(df), 0.0)

if __name__ == "__main__":
    unittest.main()
