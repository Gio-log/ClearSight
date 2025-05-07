from PyQt5.QtWidgets import QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel
from PyQt5.QtWidgets import QPushButton

def _createSniffTrafficTab():
    sniff = QWidget()
    layout = QVBoxLayout()
    label = QLabel("Sniff Traffic functionality goes here.")
    button = QPushButton("Start Sniffing")
    layout.addWidget(label)
    layout.addWidget(button)
    sniff.setLayout(layout)
    return sniff
