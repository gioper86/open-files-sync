import typer
from config_parser import ConfigParser
from command_runner import CommandRunner

app = typer.Typer()

@app.command()
def oneway(id: str, run: bool = False):
    config_parser = ConfigParser()
    command_runner = CommandRunner(config_parser.config)
    command_runner.run_rsync(id, run)

if __name__ == "__main__":
    app()