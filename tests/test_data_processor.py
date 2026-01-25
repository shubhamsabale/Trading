import unittest
from src.core.data_processor import process_positions
import pandas as pd

class TestDataProcessor(unittest.TestCase):
    def test_process_positions_empty(self):
        data = {"net": [], "day": []}
        df = process_positions(data)
        self.assertTrue(df.empty)

    def test_process_positions_with_data(self):
        data = {
            "net": [
                {
                    "tradingsymbol": "TEST",
                    "m2m": 100
                }
            ]
        }
        df = process_positions(data)
        self.assertFalse(df.empty)
        self.assertEqual(df.iloc[0]['tradingsymbol'], "TEST")
        self.assertEqual(df.iloc[0]['m2m'], 100)

if __name__ == '__main__':
    unittest.main()
