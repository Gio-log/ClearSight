import sys
import logging
import json
from PyQt5.QtWidgets import QApplication
from src.main_window import MainWindow

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def load_config():
    with open("config.json", "r") as file:
        return json.load(file)

def save_config(config):
    with open("config.json", "w") as file:
        json.dump(config, file, indent=4)

# Import the main window class from src/main_window.py
def main():
    logging.info("Starting ClearSight application...")
    try:
        config = load_config()
        app = QApplication(sys.argv)
        window = MainWindow(config=config)
        window.show()
        sys.exit(app.exec_())
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()