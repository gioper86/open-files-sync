import typer
from config_parser import ConfigParser
import subprocess

app = typer.Typer()

@app.command()
def oneway(id: str, run: bool = False):
    config_parser = ConfigParser()
    oneway_config = config_parser.oneway

    source = None
    target = None
    try:
        source = oneway_config[id]['source']
        target = oneway_config[id]['target']
    except KeyError as e:
        print(f"Error: {e}")

    rsync_command = ['rsync', '-avh', source, target]
 
    if not run:
        rsync_command.insert(2, '--dry-run')
        print("rsync running in dry run mode. Add -run argument to actually run the sync")

    try:
        result = subprocess.run(['rsync', '-avh','--dry-run', source, target], capture_output=True, text=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error: Command '{e.cmd}' failed with return code {e.returncode}")
        print(f"Standard output: {e.stdout}")
        print(f"Error output: {e.stderr}")

if __name__ == "__main__":
    app()