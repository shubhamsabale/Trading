import unittest
from src.api.kite_manager import KiteManager

class TestKiteManager(unittest.TestCase):
    def setUp(self):
        self.km = KiteManager()

    def test_mock_mode_initialization(self):
        # By default, without credentials, it should be in mock mode
        self.assertTrue(self.km.mock_mode)

    def test_get_positions_returns_dict(self):
        positions = self.km.get_positions()
        self.assertIsInstance(positions, dict)
        self.assertIn("net", positions)
        self.assertIn("day", positions)

    def test_mock_positions_content(self):
        positions = self.km.get_positions()
        net_positions = positions["net"]
        self.assertTrue(len(net_positions) > 0)
        self.assertEqual(net_positions[0]["tradingsymbol"], "RELIANCE")

if __name__ == "__main__":
    unittest.main()
