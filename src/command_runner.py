import subprocess
from rich import print
import logging

class CommandRunner:
    def __init__(self, config):
        self.config = config

    def run_rsync(self, id, run):
        logger = logging.getLogger(__name__)
        oneway_config = self.config['oneway']

        source = None
        target = None
        try:
            source = oneway_config[id]['source']
            target = oneway_config[id]['target']
        except KeyError as e:
            logger.error("Error while accessing configuration for id " + id)
            print(f"Error: {e}")
            raise

        self.__run_command(source, target, run)
    
    def __run_command(self, source, target, run):
        rsync_command = ['rsync', '-avh', source, target]
        files = []
    
        if not run:
            rsync_command.insert(2, '--dry-run')
            print("[bold yellow]Warning![/bold yellow] rsync running in dry run mode. Add -run argument to actually run the sync")

        with subprocess.Popen(rsync_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as process:

            first_line = next(process.stdout)
            print("First line: ", first_line)

            for line in process.stdout:
                if line.endswith('\n'):
                    line = line.rstrip('\n')

                if line == "":
                    break

                if not line.endswith('/'):
                    files.append(line)
                    print(line)

            stderr = process.stderr.read()
            if stderr:
                print("Standard Error:", stderr)
        print(files)
        return files
    
