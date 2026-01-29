import unittest
import pandas as pd
from src.core.data_processor import process_positions, get_total_m2m

class TestDataProcessor(unittest.TestCase):
    def setUp(self):
        self.sample_positions = {
            "net": [
                {
                    "tradingsymbol": "SYMBOL1",
                    "exchange": "NSE",
                    "quantity": 10,
                    "average_price": 100.0,
                    "last_price": 110.0,
                    "pnl": 100.0,
                    "m2m": 100.0
                },
                {
                    "tradingsymbol": "SYMBOL2",
                    "exchange": "NSE",
                    "quantity": 5,
                    "average_price": 200.0,
                    "last_price": 190.0,
                    "pnl": -50.0,
                    "m2m": -50.0
                }
            ]
        }

    def test_process_positions(self):
        df = process_positions(self.sample_positions)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df), 2)
        self.assertIn('m2m', df.columns)
        self.assertEqual(df.iloc[0]['tradingsymbol'], "SYMBOL1")

    def test_get_total_m2m(self):
        df = process_positions(self.sample_positions)
        total_m2m = get_total_m2m(df)
        self.assertEqual(total_m2m, 50.0)

    def test_process_empty_positions(self):
        df = process_positions({"net": []})
        self.assertTrue(df.empty)
        self.assertEqual(get_total_m2m(df), 0.0)

if __name__ == "__main__":
    unittest.main()
