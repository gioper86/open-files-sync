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

    # def test_run_rsync_failure(self):
    #     with patch("subprocess.run") as mock_run:
    #         mock_run.return_value.returncode = 1
    #         result = self.runner.run_rsync(456, False)
    #         mock_run.assert_called_once_with(
    #             ["/usr/bin/rsync", "/path/to/source", "/path/to/destination"],
    #             capture_output=True,
    #             text=True
    #         )
    #         self.assertEqual(result, False)

if __name__ == "__main__":
    unittest.main()