import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple PyQt5 Window")
        self.setGeometry(100, 100, 800, 600)  # x, y, width, height

        # Create the tab widget
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        # Add tabs
        self.tabs.addTab(self.create_tab("Scan Network"), "Scan Network")
        self.tabs.addTab(self.create_tab("Sniff Traffic"), "Sniff Traffic")
        self.tabs.addTab(self.create_tab("Monitor"), "Monitor")
        self.tabs.addTab(self.create_tab("Logs"), "Logs")

    def create_tab(self, title):
        """Helper method to create a tab with a label."""
        tab = QWidget()
        layout = QVBoxLayout()
        label = QLabel(f"This is the {title} tab.")
        layout.addWidget(label)
        tab.setLayout(layout)
        return tab

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())