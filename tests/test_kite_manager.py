import unittest
from src.api.kite_manager import KiteManager
from src.utils.config import Config

class TestKiteManager(unittest.TestCase):
    def test_mock_positions(self):
        # Ensure we are in mock mode for this test
        Config.MOCK_MODE = True
        manager = KiteManager()
        positions = manager.get_positions()

        self.assertIn("net", positions)
        self.assertGreater(len(positions["net"]), 0)
        self.assertEqual(positions["net"][0]["tradingsymbol"], "RELIANCE")

if __name__ == '__main__':
    unittest.main()
