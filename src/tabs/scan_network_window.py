from PyQt5.QtWidgets import QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel
from PyQt5.QtWidgets import QPushButton

def _createScanNetworkTab():
    scan = QWidget()
    layout = QVBoxLayout()
    label = QLabel("Scan Network functionality goes here.")
    button = QPushButton("Start Scan")
    layout.addWidget(label)
    layout.addWidget(button)
    scan.setLayout(layout)
    return scan
