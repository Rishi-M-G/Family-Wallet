# main_window.py

"""Main window-style application."""

import sys

from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QMainWindow,
    QStatusBar,
    QToolBar,
)

def greet():
    if msgLabel.text():
        msgLabel.setText("")
    else:
        msgLabel.setText("Hello World")

app = QApplication([])
window = QWidget()
window.setWindowTitle("Signals and Slots")
layout = QVBoxLayout()

button = QPushButton("Press Me")
button.clicked.connect(greet)

layout.addWidget(button)
msgLabel = QLabel("")
layout.addWidget(msgLabel)
window.setLayout(layout)
window.show()
sys.exit(app.exec())
