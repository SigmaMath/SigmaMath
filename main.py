from gui.main_window import mainWin
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt
import sys

""" Imported Libraries
    sys: System Library
    PySide6: PySide6 Library
"""

""" Imported Classes from PySide6 
    QApplication: Main Application Class
    QPalette: Palette Class
    QColor: Color Class
"""

""" Imported Class from gui.main_window.py
    mainWin: Custom canvas
"""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainWin()
    window.show()
    sys.exit(app.exec())
