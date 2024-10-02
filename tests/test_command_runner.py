import unittest
from unittest.mock import patch
from src.command_runner import CommandRunner
import subprocess

class TestCommandRunner(unittest.TestCase):
    def setUp(self):
        self.config = {
            "oneway": {
                "MyIphone15": {
                    "name": "My iPhone 15",
                    "id": "MyIphone15",
                    "source": "/path/source",
                    "target": "/path/target"
                }
            },
        }
        self.runner = CommandRunner(self.config)

    def test_run_rsync_success(self):
        with patch("subprocess.Popen") as mock_run:
            self.runner.run_rsync("MyIphone15", True)
            mock_run.assert_called_once_with(
                ["rsync", "-avh", "/path/source","/path/target"],
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE, 
                text=True
            )

    def test_run_rsync_success_dryrun(self):
        with patch("subprocess.Popen") as mock_run:
            self.runner.run_rsync("MyIphone15", False)
            mock_run.assert_called_once_with(
                ["rsync", "-avh", "--dry-run", "/path/source","/path/target"],
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE, 
                text=True
            )
               
    def test_run_rsync_key_error(self):
        with self.assertRaises(KeyError):
            self.runner.run_rsync("InvalidIdId", False)

if __name__ == "__main__":
    unittest.main()