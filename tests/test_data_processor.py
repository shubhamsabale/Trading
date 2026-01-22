import unittest
import pandas as pd
from src.core.data_processor import process_positions, calculate_total_mtm

class TestDataProcessor(unittest.TestCase):
    def setUp(self):
        self.mock_positions_data = {
            "net": [
                {
                    "tradingsymbol": "SBIN",
                    "quantity": 100,
                    "average_price": 500.0,
                    "last_price": 520.0,
                    "m2m": 2000.0,
                },
                {
                    "tradingsymbol": "INFY",
                    "quantity": 50,
                    "average_price": 1500.0,
                    "last_price": 1450.0,
                    "m2m": -2500.0,
                }
            ]
        }

    def test_process_positions(self):
        df = process_positions(self.mock_positions_data)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df), 2)
        self.assertIn('calculated_mtm', df.columns)
        self.assertEqual(df.iloc[0]['calculated_mtm'], 2000.0)
        self.assertEqual(df.iloc[1]['calculated_mtm'], -2500.0)

    def test_calculate_total_mtm(self):
        df = process_positions(self.mock_positions_data)
        total_mtm = calculate_total_mtm(df)
        self.assertEqual(total_mtm, -500.0)

    def test_empty_positions(self):
        df = process_positions({"net": []})
        self.assertTrue(df.empty)
        self.assertEqual(calculate_total_mtm(df), 0.0)

if __name__ == "__main__":
    unittest.main()
