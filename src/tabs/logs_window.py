from PyQt5.QtWidgets import QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel

def _createLogsTab():
    logs = QWidget()
    layout = QVBoxLayout()
    label = QLabel("Logs functionality goes here.")
    layout.addWidget(label)
    logs.setLayout(layout)
    return logs