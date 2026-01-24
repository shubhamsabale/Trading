import unittest
import pandas as pd
from src.core.data_processor import process_positions, get_total_mtm

class TestDataProcessor(unittest.TestCase):
    def test_process_positions(self):
        mock_data = {
            "net": [
                {
                    "tradingsymbol": "TEST1",
                    "quantity": 10,
                    "average_price": 100.0,
                    "last_price": 110.0
                },
                {
                    "tradingsymbol": "TEST2",
                    "quantity": 5,
                    "average_price": 200.0,
                    "last_price": 190.0
                }
            ]
        }
        df = process_positions(mock_data)

        self.assertEqual(len(df), 2)
        # (110 - 100) * 10 = 100
        self.assertEqual(df.iloc[0]['calculated_mtm'], 100.0)
        # (190 - 200) * 5 = -50
        self.assertEqual(df.iloc[1]['calculated_mtm'], -50.0)

    def test_get_total_mtm(self):
        df = pd.DataFrame({
            'calculated_mtm': [100.0, -50.0, 25.0]
        })
        total = get_total_mtm(df)
        self.assertEqual(total, 75.0)

    def test_empty_positions(self):
        df = process_positions({"net": []})
        self.assertTrue(df.empty)
        self.assertEqual(get_total_mtm(df), 0.0)

if __name__ == '__main__':
    unittest.main()
