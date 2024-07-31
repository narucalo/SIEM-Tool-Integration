import unittest
from scripts.search_data import load_config, connect_to_splunk

class TestSearchData(unittest.TestCase):
    def test_load_config(self):
        config = load_config()
        self.assertIn('host', config)
        self.assertIn('port', config)
        self.assertIn('username', config)
        self.assertIn('password', config)

    def test_connect_to_splunk(self):
        config = load_config()
        service = connect_to_splunk(config)
        self.assertIsNotNone(service)

if __name__ == '__main__':
    unittest.main()
