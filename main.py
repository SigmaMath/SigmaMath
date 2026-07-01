from gui.main_window import mainWin
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QPalette, QColor, QIcon
from PySide6.QtCore import Qt
import sys
import ctypes

""" Imported Libraries
    sys: System Library
    PySide6: PySide6 Library
    ctypes: ctypes Library for Windows OS specific functions
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
    """
    For Windows > Assigns a unique ID to the application
                > So the application can be identified as an app and not a 
                > Sets the icon for the application
    """
    if sys.platform == "win32":
        my_app_id = "SigmaMath"  # Any unique string works
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(my_app_id) # setting the app id
    
    app = QApplication(sys.argv)
    window = mainWin()
    window.show()
    sys.exit(app.exec())
