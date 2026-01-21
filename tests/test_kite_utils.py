import unittest
from kite_utils import KiteManager

class TestKiteManager(unittest.TestCase):
    def test_mock_mode(self):
        km = KiteManager(mock=True)
        self.assertTrue(km.mock)
        positions = km.get_positions()
        self.assertIsNotNone(positions)
        self.assertIn('net', positions)
        self.assertEqual(len(positions['net']), 3)

if __name__ == '__main__':
    unittest.main()
