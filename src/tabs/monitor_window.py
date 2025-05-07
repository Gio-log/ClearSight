from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

def _createMonitorTab():
    monitor = QWidget()
    layout = QVBoxLayout()
    label = QLabel("Monitor functionality goes here.")
    layout.addWidget(label)
    monitor.setLayout(layout)
    return monitor
