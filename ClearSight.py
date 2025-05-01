import sys
import logging
from PyQt5.QtWidgets import QApplication
from src.main_window import MainWindow

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Import the main window class from src/main_window.py
def main():
    logging.info("Starting ClearSight application...")
    try:
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()