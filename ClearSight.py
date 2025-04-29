import sys
from PyQt5.QtWidgets import QApplication
from src.main_window import MainWindow

# Import the main window class from src/main_window.py
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()