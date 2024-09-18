import yaml

class ConfigParser:
    def __init__(self):
        self.oneway = {}
        self._CONFIG_PATH = '../example-config/config.yaml' 
        self.parse_config(self._CONFIG_PATH)

    def parse_config(self, file_path):
        with open(file_path, 'r') as file:
            config_data = yaml.safe_load(file)
            for location in config_data['one-way-sync-locations']:
                self.oneway[location["id"]] = location
        return config_data
