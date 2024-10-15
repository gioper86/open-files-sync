import unittest
from unittest.mock import patch, MagicMock
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

    def test_rsync_output(self):
        with patch("subprocess.Popen") as mock_popen:
            mock_process = MagicMock()

            rsync_output = [
                "building file list ... done\n",
                "src/\n",
                "src/components/\n",
                "src/components/BottomPanel.js\n",
                "src/components/NavBar.js\n",
                "src/components/layout.js\n",
                "src/components/panel.scss\n",
                "src/images/\n",
                "src/images/icon.png\n",
                "src/images/logo.png\n",
                "\n",
                "sent 710.72K bytes  received 396 bytes  1.42M bytes/sec\n",
                "total size is 709.37K  speedup is 1.00\n"
            ]

            mock_process.stdout = iter(rsync_output)
            mock_process.stderr.read = lambda: "some error"
            mock_popen.return_value.__enter__.return_value = mock_process

            files = self.runner._CommandRunner__run_command("a", "b", False)
            self.assertEqual(len(files), 6)

if __name__ == "__main__":
    unittest.main()