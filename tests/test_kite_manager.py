import unittest
from unittest.mock import MagicMock, patch
from src.api.kite_manager import KiteManager

class TestKiteManager(unittest.TestCase):
    @patch('src.api.kite_manager.Config')
    def test_mock_mode_init(self, mock_config):
        mock_config.MOCK_MODE = True
        km = KiteManager()
        self.assertTrue(km.mock_mode)
        self.assertIsNone(km.kite)

    @patch('src.api.kite_manager.Config')
    @patch('src.api.kite_manager.KiteConnect')
    def test_real_mode_init(self, mock_kite_connect, mock_config):
        mock_config.MOCK_MODE = False
        mock_config.KITE_API_KEY = "test_key"
        mock_config.KITE_API_SECRET = "test_secret"
        mock_config.KITE_ACCESS_TOKEN = "test_token"

        km = KiteManager()
        self.assertFalse(km.mock_mode)
        self.assertIsNotNone(km.kite)
        mock_kite_connect.assert_called_with(api_key="test_key")
        km.kite.set_access_token.assert_called_with("test_token")

    def test_get_positions_mock(self):
        # We don't need to patch Config here if we just want to test if it returns mock data
        with patch('src.api.kite_manager.Config') as mock_config:
            mock_config.MOCK_MODE = True
            km = KiteManager()
            positions = km.get_positions()
            self.assertIn('net', positions)
            self.assertGreater(len(positions['net']), 0)
            self.assertEqual(positions['net'][0]['tradingsymbol'], 'SBIN')

if __name__ == "__main__":
    unittest.main()
