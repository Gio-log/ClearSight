import sys
import logging
import json
from PyQt5.QtWidgets import QApplication
from src.main_window import MainWindow

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("clearsight.log"),
        logging.StreamHandler()
    ]
)

def loadConfig():
    try:
        with open("config.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        logging.warning("Configuration file not found. Creating a default configuration.")
        default_config = {
            "appName": "ClearSight",
            "version": "1.0.0",
            "stylesheets": [],
            "last_stylesheet": None
        }
        saveConfig(default_config)
        return default_config
    except json.JSONDecodeError:
        logging.error("Configuration file is corrupted. Please fix or delete it.")
        sys.exit(1)

def saveConfig(config):
    with open("config.json", "w") as file:
        json.dump(config, file, indent=4)

def main():
    logging.info("Starting ClearSight application...")
    try:
        config = loadConfig()
        app = QApplication(sys.argv)
        window = MainWindow(config=config)
        window.show()
        sys.exit(app.exec_())
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()