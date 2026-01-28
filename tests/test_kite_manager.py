import unittest
from unittest.mock import patch, MagicMock
from src.api.kite_manager import KiteManager

class TestKiteManager(unittest.TestCase):
    @patch('src.api.kite_manager.Config')
    def test_mock_mode_behavior(self, mock_config):
        # Test that it uses mock data when MOCK_MODE is True
        mock_config.is_mock_mode.return_value = True
        km = KiteManager()
        positions = km.get_positions()
        self.assertIn('net', positions)
        self.assertTrue(len(positions['net']) > 0)
        self.assertEqual(positions['net'][0]['tradingsymbol'], "SBIN")

    @patch('src.api.kite_manager.KiteConnect')
    @patch('src.api.kite_manager.Config')
    def test_real_mode_behavior(self, mock_config, mock_kite_connect):
        # Test that it calls KiteConnect when MOCK_MODE is False
        mock_config.is_mock_mode.return_value = False
        mock_config.KITE_API_KEY = "test_key"
        mock_config.KITE_ACCESS_TOKEN = "test_token"

        km = KiteManager()
        km.kite.positions = MagicMock(return_value={"net": [{"symbol": "REAL"}]})

        positions = km.get_positions()
        km.kite.positions.assert_called_once()
        self.assertEqual(positions['net'][0]['symbol'], "REAL")

if __name__ == '__main__':
    unittest.main()
