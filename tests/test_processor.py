import unittest
import pandas as pd
from src.core.data_processor import process_positions

class TestDataProcessor(unittest.TestCase):
    def test_process_positions(self):
        mock_data = {
            "net": [
                {"tradingsymbol": "TEST1", "m2m": 100.0, "pnl": 90.0, "quantity": 1},
                {"tradingsymbol": "TEST2", "m2m": -50.0, "pnl": -60.0, "quantity": 2},
            ]
        }
        df = process_positions(mock_data)
        self.assertEqual(len(df), 2)
        self.assertEqual(df.iloc[0]['tradingsymbol'], "TEST1")
        self.assertEqual(df.iloc[1]['m2m'], -50.0)

    def test_empty_positions(self):
        df = process_positions({"net": []})
        self.assertTrue(df.empty)

if __name__ == "__main__":
    unittest.main()
