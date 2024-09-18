import unittest
from src.config_parser import ConfigParser
from unittest.mock import mock_open, patch

config_mock = """
one-way-sync-locations:
  - name: "My iPhone 15"
    id: "MyIphone15"
    source: "/Users/myuser/Documents/rsynctest/source"
    target: "/Users/myuser/Documents/rsynctest/target"
  - name: "GoPro SD Card"
    id: "GoproSDCard"
    source: "/someFolder/someOtherFolder"
    target: "/Users/myuser/Documents/rsynctest/target"
    """

class ConfigParserTests(unittest.TestCase):
    
    @patch('src.config_parser.open', new_callable=mock_open, read_data=config_mock)
    def test_parse_config(self, mock_file):
        parser = ConfigParser()
        mock_file.assert_called_once_with(parser._CONFIG_PATH, 'r')

        self.assertIn('MyIphone15', parser.oneway)
        self.assertIn('GoproSDCard', parser.oneway)
        self.assertEqual(parser.oneway['MyIphone15']['name'], "My iPhone 15")
        self.assertEqual(parser.oneway['GoproSDCard']['name'], "GoproSDCard")
    
    #TODO handle cases of malformed YAML, missing properties etc..

if __name__ == "__main__":
    unittest.main()