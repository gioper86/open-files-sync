import yaml
import os

class ConfigParser:
    def __init__(self):
        self.config = {
            "oneway": {}
        }
        self._CONFIG_PATH = '~/.openfilessync/config.yaml' 
        file_path = os.path.expanduser(self._CONFIG_PATH)
        self.parse_config(file_path)

    def parse_config(self, file_path):
        with open(file_path, 'r') as file:
            config_data = yaml.safe_load(file)
            for location in config_data['one-way-sync-locations']:
                self.config["oneway"][location["id"]] = location
        return config_data
    
