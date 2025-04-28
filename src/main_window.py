import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel, QPushButton
from tabs.scan_network_window import create_scan_network_tab
from tabs.sniff_traffic_window import create_sniff_traffic_tab
from tabs.monitor_window import create_monitor_tab
from tabs.logs_window import create_logs_tab

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Stylized PyQt5 Window")
        self.setGeometry(100, 100, 488, 600)
        self.setMinimumSize(488, 600)

        stylesheet_path = os.path.join(os.path.dirname(__file__), "../assets/style.qss")
        self.load_stylesheet(stylesheet_path)

        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.tabs.addTab(create_scan_network_tab(), "Scan Network")
        self.tabs.addTab(create_sniff_traffic_tab(), "Sniff Traffic")
        self.tabs.addTab(create_monitor_tab(), "Monitor")
        self.tabs.addTab(create_logs_tab(), "Logs")

    def load_stylesheet(self, filename):
        try:
            with open(filename, "r") as file:
                self.setStyleSheet(file.read())
        except FileNotFoundError:
            print(f"Stylesheet file '{filename}' not found.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())