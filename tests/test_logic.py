import unittest
import pandas as pd
from src.core.data_processor import calculate_mtm
from src.api.kite_manager import KiteManager

class TestTradingLogic(unittest.TestCase):
    def test_calculate_mtm(self):
        positions = {
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
        df = calculate_mtm(positions)
        self.assertEqual(len(df), 2)
        # (110 - 100) * 10 = 100
        self.assertEqual(df[df['tradingsymbol'] == 'TEST1']['mtm'].values[0], 100.0)
        # (190 - 200) * 5 = -50
        self.assertEqual(df[df['tradingsymbol'] == 'TEST2']['mtm'].values[0], -50.0)

    def test_kite_manager_mock(self):
        km = KiteManager()
        # Mock mode should be True by default in our setup if no keys are provided
        self.assertTrue(km.mock_mode)
        positions = km.get_positions()
        self.assertIn('net', positions)
        self.assertTrue(len(positions['net']) > 0)

if __name__ == '__main__':
    unittest.main()
