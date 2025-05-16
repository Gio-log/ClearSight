from PyQt5.QtWidgets import QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel, QTextEdit
import os

LOG_FILE = "clearsight.log"  # Adjust path if needed

def _createLogsTab():
    logs = QWidget()
    layout = QVBoxLayout()

    label = QLabel("Application Logs:")
    layout.addWidget(label)

    log_view = QTextEdit()
    log_view.setReadOnly(True)

    # Load log file contents
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            log_view.setPlainText(f.read())
    else:
        log_view.setPlainText("Log file not found.")

    layout.addWidget(log_view)
    logs.setLayout(layout)
    return logs