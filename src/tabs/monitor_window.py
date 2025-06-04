from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtChart import QChart, QChartView, QLineSeries
from PyQt5.QtGui import QPainter

def _createMonitorTab():
    monitor = QWidget()
    layout = QVBoxLayout()
    label = QLabel("Graph to show collected data will be here. (placeholder)")
    layout.addWidget(label)

    # Function to (re)generate the chart data
    def refresh_chart():
        series = QLineSeries()
        # Example data, you can replace this with dynamic data
        series.append(0, 6)
        series.append(1, 4)
        series.append(2, 8)
        series.append(3, 3)
        series.append(4, 7)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Example Monitor Graph")
        chart.createDefaultAxes()
        chart_view.setChart(chart)

    chart_view = QChartView()
    chart_view.setRenderHint(QPainter.Antialiasing)
    layout.addWidget(chart_view)

    refresh_btn = QPushButton("Refresh")
    refresh_btn.clicked.connect(refresh_chart)
    layout.addWidget(refresh_btn)

    monitor.setLayout(layout)

    # Initial chart load
    refresh_chart()

    return monitor
