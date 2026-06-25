import sys
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QDialog,
    QLineEdit,
    QVBoxLayout,
    QMainWindow,
)
from PySide6.QtCore import Slot, QObject, Signal
from PySide6.QtGui import QIcon

""" Imported Libraries
    sys: System Library
    PySide6: PySide6 Library
"""

""" Imported Classes from PySide6 
    QApplication: Main Application Class
    QLabel: Label Class
    QPushButton: Button Class
    QDialog: Dialog Class
    QLineEdit: Line Edit Class
    QVBoxLayout: Vertical Layout Class
    QMainWindow: Main Window Class
    Slot: Slot Class
    QObject: Object Class
    Signal: Signal Class
    QIcon: Icon Class
"""

""" Main Window Class
    This will be the main Canvas of the program in which every element (Widget) will be placed
    It inherits from QMainWindow 
"""


class mainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SigmaMath")
        self.setWindowIcon(QIcon("icon\sigma.png"))
        self.setMinimumSize(450, 600)

    """ 
    Reads the external QSS file and applies it globally to the window.
    """

    def load_stylesheet(self):
        try:
            with open("gui/style.qss", "r") as f:
                style_data = f.read()
                self.setStyleSheet(style_data)
        except FileNotFoundError:
            print("Warning: style.qss not found. Running with default system theme.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainWin()
    window.show()
    sys.exit(app.exec())
