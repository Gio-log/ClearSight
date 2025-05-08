import json
import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QFileDialog, QMenu, QAction
from .tabs.scan_network_window import _createScanNetworkTab
from .tabs.sniff_traffic_window import _createSniffTrafficTab
from .tabs.monitor_window import _createMonitorTab
from .tabs.logs_window import _createLogsTab

class MainWindow(QMainWindow):
    def __init__(self, config=None):
        super().__init__()
        self.config = config or {}
        self.saved_stylesheets = self.config.get("stylesheets", [])
        self.initUI()

        # Autoload the last used stylesheet if available
        if self.saved_stylesheets:
            last_stylesheet = self.saved_stylesheets[-1]  # Load the most recently saved stylesheet
            self._loadStylesheet(last_stylesheet)

    def initUI(self):
        self.setWindowTitle("Stylized PyQt5 Window")
        self.setGeometry(100, 100, 488, 600)
        self.setMinimumSize(488, 600)

        if self.config and "title" in self.config:
            self.setWindowTitle(self.config["title"])

        self._createMenuBar()

        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.tabs.addTab(_createScanNetworkTab(), "Scan Network")
        self.tabs.addTab(_createSniffTrafficTab(), "Sniff Traffic")
        self.tabs.addTab(_createMonitorTab(), "Monitor")
        self.tabs.addTab(_createLogsTab(), "Logs")

    def _createMenuBar(self):
        """Create the menu bar with options."""
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu("File")
        chooseStylesheetAction = QAction("Choose Stylesheet", self)
        chooseStylesheetAction.triggered.connect(self._chooseStylesheet)
        fileMenu.addAction(chooseStylesheetAction)

        if self.saved_stylesheets:
            for stylesheet in self.saved_stylesheets:
                action = QAction(f"Load {os.path.basename(stylesheet)}", self)
                action.triggered.connect(lambda checked, path=stylesheet: self._loadStylesheet(path))
                fileMenu.addAction(action)

        editMenu = menuBar.addMenu("Edit")
        helpMenu = menuBar.addMenu("Help")

    def _chooseStylesheet(self):
        """Open a file dialog to choose a stylesheet."""
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(self, "Choose Stylesheet", "", "Stylesheet Files (*.qss);;All Files (*)", options=options)
        if filename:
            self._loadStylesheet(filename)

            if filename not in self.saved_stylesheets:
                self.saved_stylesheets.append(filename)
                self.config["stylesheets"] = self.saved_stylesheets
                self._saveConfig()

    def _loadStylesheet(self, filename):
        """Load the stylesheet from a file."""
        try:
            with open(filename, "r") as file:
                self.setStyleSheet(file.read())
        except FileNotFoundError:
            print(f"Stylesheet file '{filename}' not found.")

    def _saveConfig(self):
        """Save the updated configuration to the config file."""
        if not isinstance(self.config, dict):
            print("Error: Configuration is not a valid dictionary. Skipping save.")
            return
        with open("config.json", "w") as file:
            json.dump(self.config, file, indent=4)


if __name__ == "__main__":
    # Load configuration from file
    config = {}
    if os.path.exists("config.json"):
        with open("config.json", "r") as file:
            config = json.load(file)

    app = QApplication(sys.argv)
    window = MainWindow(config=config)
    window.show()
    sys.exit(app.exec_())