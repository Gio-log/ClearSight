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
        self.last_stylesheet = self.config.get("last_stylesheet", None)
        self.initUI()

        # Autoload the last chosen stylesheet if available
        if self.last_stylesheet and os.path.exists(self.last_stylesheet):
            print(f"Loading last stylesheet: {self.last_stylesheet}")
            self._loadStylesheet(self.last_stylesheet)
        elif self.last_stylesheet:
            print(f"Warning: Last stylesheet '{self.last_stylesheet}' not found.")

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

        # Add "About/Info" action to Help menu that shows a notification
        helpAction = QAction("About", self)
        helpAction.triggered.connect(self._showHelpNotification)
        helpMenu.addAction(helpAction)

    def _showHelpNotification(self):
        from PyQt5.QtWidgets import QMessageBox
        QMessageBox.information(self, "Help", "This feature is in development.")

    def _chooseStylesheet(self):
        """Open a file dialog to choose a stylesheet."""
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(self, "Choose Stylesheet", "", "Stylesheet Files (*.qss);;All Files (*)", options=options)
        if filename:
            self._loadStylesheet(filename)

            self.last_stylesheet = filename
            self.config["last_stylesheet"] = self.last_stylesheet

            if filename not in self.saved_stylesheets:
                self.saved_stylesheets.append(filename)
                self.config["stylesheets"] = self.saved_stylesheets

            self._saveConfig()

    def _loadStylesheet(self, filename):
        """Load the stylesheet from a file."""
        try:
            with open(filename, "r") as file:
                self.setStyleSheet(file.read())
            self.last_stylesheet = filename
            self.config["last_stylesheet"] = self.last_stylesheet
            self._saveConfig()
            print(f"Stylesheet '{filename}' loaded successfully.")
        except FileNotFoundError:
            print(f"Error: Stylesheet file '{filename}' not found.")
        except Exception as e:
            print(f"Error: Failed to load stylesheet '{filename}'. Reason: {e}")

    def _saveConfig(self):
        """Save the updated configuration to the config file."""
        if not isinstance(self.config, dict):
            print("Error: Configuration is not a valid dictionary. Skipping save.")
            return
        try:
            with open("config.json", "w") as file:
                json.dump(self.config, file, indent=4)
            print("Configuration saved successfully.")
        except Exception as e:
            print(f"Error: Failed to save configuration. Reason: {e}")


if __name__ == "__main__":
    config = {}
    if os.path.exists("config.json"):
        with open("config.json", "r") as file:
            config = json.load(file)

    app = QApplication(sys.argv)
    window = MainWindow(config=config)
    window.show()
    sys.exit(app.exec_())