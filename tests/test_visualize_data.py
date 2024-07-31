import unittest
from scripts.visualize_data import load_processed_data

class TestVisualizeData(unittest.TestCase):
    def test_load_processed_data(self):
        data = load_processed_data('data/processed_data.json')
        self.assertIsInstance(data, dict)

if __name__ == '__main__':
    unittest.main()
