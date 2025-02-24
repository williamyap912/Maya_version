# Configuration Settings
import os

SAVE_PATH = os.path.expanduser("~/maya/version_control/")
LOG_FILE = os.path.expanduser("~/maya/version_control/log.txt")

def ensure_directory():
    """Ensure save directory exists."""
    if not os.path.exists(SAVE_PATH):
        os.makedirs(SAVE_PATH)
