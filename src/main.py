import typer
from config_parser import ConfigParser
from command_runner import CommandRunner
import logger_util
import logging

app = typer.Typer()

@app.command()
def oneway(id: str, run: bool = False):
    logger_util.setup_logging()
    logger = logging.getLogger(__name__)

    config_parser = ConfigParser()
    command_runner = CommandRunner(config_parser.config)
    command_runner.run_rsync(id, run)
 
if __name__ == "__main__":
    app()
