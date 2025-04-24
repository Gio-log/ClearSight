import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stylized PyQt5 Window")
        self.setGeometry(100, 100, 800, 600)  # x, y, width, height

        # Load the external stylesheet
        stylesheet_path = os.path.join(os.path.dirname(__file__), "../assets/style.qss")
        self.load_stylesheet(stylesheet_path)

        # Create the tab widget
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        # Add tabs with specific content
        self.tabs.addTab(self.create_scan_network_tab(), "Scan Network")
        self.tabs.addTab(self.create_sniff_traffic_tab(), "Sniff Traffic")
        self.tabs.addTab(self.create_monitor_tab(), "Monitor")
        self.tabs.addTab(self.create_logs_tab(), "Logs")

    def load_stylesheet(self, filename):
        """Load the stylesheet from an external file."""
        try:
            with open(filename, "r") as file:
                self.setStyleSheet(file.read())
        except FileNotFoundError:
            print(f"Stylesheet file '{filename}' not found.")

    def create_scan_network_tab(self):
        """Create the Scan Network tab."""
        tab = QWidget()
        layout = QVBoxLayout()
        label = QLabel("Scan Network functionality goes here.")
        button = QPushButton("Start Scan")
        layout.addWidget(label)
        layout.addWidget(button)
        tab.setLayout(layout)
        return tab

    def create_sniff_traffic_tab(self):
        """Create the Sniff Traffic tab."""
        tab = QWidget()
        layout = QVBoxLayout()
        label = QLabel("Sniff Traffic functionality goes here.")
        button = QPushButton("Start Sniffing")
        layout.addWidget(label)
        layout.addWidget(button)
        tab.setLayout(layout)
        return tab

    def create_monitor_tab(self):
        """Create the Monitor tab."""
        tab = QWidget()
        layout = QVBoxLayout()
        label = QLabel("Monitor functionality goes here.")
        layout.addWidget(label)
        tab.setLayout(layout)
        return tab

    def create_logs_tab(self):
        """Create the Logs tab."""
        tab = QWidget()
        layout = QVBoxLayout()
        label = QLabel("Logs functionality goes here.")
        layout.addWidget(label)
        tab.setLayout(layout)
        return tab

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())