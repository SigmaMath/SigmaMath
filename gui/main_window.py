import sys
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QDialog,
    QLineEdit,
    QVBoxLayout,
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QStackedWidget,
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
    QHBoxLayout: Horizontal Layout Class
    QWidget: Widget Class
    QMainWindow: Main Window Class
    QStackedWidget: Stacked Widget Class
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

        # title and icon
        self.setWindowTitle("SigmaMath")
        self.setWindowIcon(QIcon("icon\sigma.png"))

        # base size when opened
        self.setMinimumSize(450, 600)

        # creating custom interface using blank canvas (QWidget)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        # creating master layout
        self.masterLayout = QHBoxLayout(self.centralWidget)
        self.masterLayout.setContentsMargins(0, 0, 0, 0)
        self.masterLayout.setSpacing(0)

        # creating sidebar
        self.sidebarWidget = QWidget()
        self.sidebar_layout = QVBoxLayout(self.sidebarWidget)
        

        # creating view stack
        self.view_stack = QStackedWidget()
        self.masterLayout.addWidget(self.view_stack, stretch=1)

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
