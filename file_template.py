import os
from pathlib import Path
import logging 

logging.basicConfig( level=logging.INFO, format = '[%(asctime)s] : %(message)s')

list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    ".env",
    "setup.py",
    "app.py",
    "src/prompt.py",
    "research/trials.ipynb"
]

for file in list_of_files:
    file_path = Path(file)
    file_dir = file_path.parent
    if not os.path.exists(file_dir):
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Directory {file_dir} created.")
    else:
        logging.info(f"Directory {file_dir} already exists.")
    
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            pass  # Create an empty file
        logging.info(f"File {file_path} created.")
    else:
        logging.info(f"File {file_path} already exists.")

