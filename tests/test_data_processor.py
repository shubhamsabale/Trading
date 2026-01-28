import unittest
import pandas as pd
from src.core.data_processor import process_positions, calculate_total_mtm

class TestDataProcessor(unittest.TestCase):
    def setUp(self):
        self.sample_data = {
            "net": [
                {"tradingsymbol": "ABC", "m2m": 100.0, "quantity": 10},
                {"tradingsymbol": "XYZ", "m2m": -50.0, "quantity": 5}
            ]
        }

    def test_process_positions(self):
        df = process_positions(self.sample_data)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df), 2)
        self.assertIn('tradingsymbol', df.columns)
        self.assertIn('m2m', df.columns)
        self.assertEqual(df.iloc[0]['tradingsymbol'], "ABC")

    def test_calculate_total_mtm(self):
        df = process_positions(self.sample_data)
        total = calculate_total_mtm(df)
        self.assertEqual(total, 50.0)

    def test_empty_positions(self):
        df = process_positions({"net": []})
        self.assertTrue(df.empty)
        self.assertEqual(calculate_total_mtm(df), 0.0)

if __name__ == '__main__':
    unittest.main()
