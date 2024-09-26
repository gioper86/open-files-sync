import logging
import os

def setup_logging():
    file_path = '~/.openfilessync/app.log' 
    file_path = os.path.expanduser(file_path)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(file_path),
        ]
    )
