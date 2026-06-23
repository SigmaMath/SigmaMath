import sys
from PySide6.QtWidgets import QApplication, QLabel

# Create the application object
app = QApplication(sys.argv)

# Create a label
label = QLabel("PySide6 Installed Successfully!")
label.show()

# Run the app
sys.exit(app.exec())