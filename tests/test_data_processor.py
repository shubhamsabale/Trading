import unittest
import pandas as pd
from src.core.data_processor import DataProcessor

class TestDataProcessor(unittest.TestCase):
    def test_process_positions(self):
        mock_data = {
            "net": [
                {
                    "tradingsymbol": "TEST",
                    "pnl": 100.0,
                    "m2m": 100.0,
                    "extra": "ignore"
                }
            ]
        }
        df = DataProcessor.process_positions(mock_data)

        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df), 1)
        self.assertIn("tradingsymbol", df.columns)
        self.assertIn("pnl", df.columns)
        self.assertIn("m2m", df.columns)
        self.assertNotIn("extra", df.columns)
        self.assertEqual(df.iloc[0]["tradingsymbol"], "TEST")

if __name__ == '__main__':
    unittest.main()
