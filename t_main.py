"""Simple Hello, World Example with PyQt6"""
# Step 1
import sys
from PyQt6.QtWidgets import QApplication,QLabel,QWidget

# Step 2
app = QApplication([])

# Step 3
window = QWidget()
window.setWindowTitle("PyQt App")
window.setGeometry(100,100,280,80)
helloMsg = QLabel("<h1>Hello, World!</h1>",parent=window)
helloMsg.move(60,15)

# Step 4
window.show()

# Step 5
sys.exit(app.exec())

