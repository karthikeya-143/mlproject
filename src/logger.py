import logging
import os
from datetime import datetime

# Get project root directory (IMPORTANT)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

# Create logs folder in project root
logs_path = os.path.join(BASE_DIR, "logs")
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)

if __name__ == "__main__":
    logging.info("Logging has started.")
    print("Log file created at:", LOG_FILE_PATH)