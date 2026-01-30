import unittest
import pandas as pd
from src.core.data_processor import process_positions, calculate_total_mtm

class TestDataProcessor(unittest.TestCase):
    def test_process_positions(self):
        mock_data = {
            "net": [
                {"tradingsymbol": "TEST", "exchange": "NSE", "quantity": 10, "last_price": 100.0, "m2m": 50.0, "pnl": 50.0}
            ]
        }
        df = process_positions(mock_data)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertFalse(df.empty)
        self.assertEqual(df.iloc[0]['tradingsymbol'], "TEST")

    def test_calculate_total_mtm(self):
        df = pd.DataFrame([
            {"m2m": 100.0},
            {"m2m": -50.0}
        ])
        total_mtm = calculate_total_mtm(df)
        self.assertEqual(total_mtm, 50.0)

if __name__ == '__main__':
    unittest.main()
