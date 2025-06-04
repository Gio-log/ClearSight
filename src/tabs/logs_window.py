from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton
import os

LOG_FILE = "clearsight.log"  # Adjust path if needed

def _createLogsTab():
    logs = QWidget()
    layout = QVBoxLayout()

    label = QLabel("Application Logs:")
    layout.addWidget(label)

    log_view = QTextEdit()
    log_view.setReadOnly(True)

    def refresh_chart():
        # Clear the log view and reload the log file
        log_view.clear()
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, "r", encoding="utf-8") as f:
                log_view.setPlainText(f.read())
        else:
            log_view.setPlainText("Log file not found.")

    def clear_chart():
        # Clear the log file
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, "w", encoding="utf-8") as f:
                f.write("")
            log_view.clear()
            log_view.setPlainText("Log file cleared.")
        else:
            log_view.setPlainText("Log file not found.")

    refresh_btn = QPushButton("Refresh")
    refresh_btn.clicked.connect(refresh_chart)
    clear_btn = QPushButton("Clear")
    clear_btn.clicked.connect(clear_chart)
    layout.addWidget(log_view)
    layout.addWidget(refresh_btn)
    layout.addWidget(clear_btn)

    logs.setLayout(layout)

    refresh_chart()

    return logs