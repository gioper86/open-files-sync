import subprocess
from rich import print

class CommandRunner:
    def __init__(self, config):
        self.config = config

    def run_rsync(self, id, run):
        oneway_config = self.config['oneway']

        source = None
        target = None
        try:
            source = oneway_config[id]['source']
            target = oneway_config[id]['target']
        except KeyError as e:
            print(f"Error: {e}")

        rsync_command = ['rsync', '-avh', source, target]
    
        if not run:
            rsync_command.insert(2, '--dry-runsks')
            print("[bold yellow]Warning![/bold yellow] rsync running in dry run mode. Add -run argument to actually run the sync")

        try:
            result = subprocess.run(rsync_command, capture_output=True, text=True, check=True)
            print(result)
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Error: Command '{e.cmd}' failed with return code {e.returncode}")
            print(f"Standard output: {e.stdout}")
            print(f"Error output: {e.stderr}")
