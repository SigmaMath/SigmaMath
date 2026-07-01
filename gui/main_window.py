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
    QSizePolicy,
    QSpacerItem,
)
from PySide6.QtCore import Slot, QObject, Signal, Qt
from PySide6.QtGui import QIcon, QPixmap
from gui.views.basic import basic

""" Imported Libraries
    PySide6: PySide6 Library
    basic: custom basic view
    basic: custom basic view
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
    QHBoxLayout: Horizontal Layout Class
    QWidget: Widget Class
    QMainWindow: Main Window Class
    QStackedWidget: Stacked Widget Class
    QStackedWidget: Stacked Widget Class
    Slot: Slot Class
    QObject: Object Class
    Signal: Signal Class
    QIcon: Icon Class
    QIcon: Icon Class
"""

""" Main Window Class
    This will be the main Canvas of the program in which every element (Widget) will be placed
    It inherits from QMainWindow 
    It inherits from QMainWindow 
"""


class mainWin(QMainWindow):
    def __init__(self):
        super().__init__()
         
        self.setWindowIcon(QIcon("icon/sigmaW.png"))

        # base size when opened
        self.setMinimumSize(460, 600)

        # creating custom interface using blank canvas (QWidget)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        # removing the window frame
        self.setWindowFlags(Qt.FramelessWindowHint)  # removing the window frame
        self.setAttribute(Qt.WA_TranslucentBackground)  # removing the window background

        # creating a Custom title bar
        self.titlebar = QWidget()
        self.titlebar.setObjectName("titlebar")
        self.titlebar.setFixedHeight(32)

        titlebar_layout = QHBoxLayout(self.titlebar)
        titlebar_layout.setContentsMargins(10, 0, 0, 0)
        titlebar_layout.setSpacing(5)

        icon_img = QPixmap("icon/sigmaW.png")  # load icon
        icon_scaled = icon_img.scaled(16, 16, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.icon = QLabel()
        self.icon.setPixmap(icon_scaled)
        self.title = QLabel("SigmaMath")  # set title
        self.title.setStyleSheet("color: #fff; font-size = 12; font-family: 'Segoe UI';")

        titlebar_layout.addWidget(self.icon)
        titlebar_layout.addWidget(self.title)

        titlebar_layout.addSpacerItem(
            QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        )  # Spacer to push buttons to the right

        # creating buttons
        self.btn_minimize = QPushButton("─")
        self.btn_maximize = QPushButton("🗖")
        self.btn_close = QPushButton("✕")

        self.btn_minimize.setObjectName("TitleBtn")
        self.btn_maximize.setObjectName("TitleBtn")
        self.btn_close.setObjectName("TitleBtnClose")

        # calling buttons functions
        self.btn_minimize.clicked.connect(self.showMinimized)
        self.btn_maximize.clicked.connect(self.toggleMaximize)
        self.btn_close.clicked.connect(self.close)

        titlebar_layout.addWidget(self.btn_minimize)
        titlebar_layout.addWidget(self.btn_maximize)
        titlebar_layout.addWidget(self.btn_close)

        # creating master layout
        self.masterLayout = QVBoxLayout(self.centralWidget)
        self.masterLayout.setContentsMargins(0, 0, 0, 0)
        self.masterLayout.setSpacing(0)

        # creating sidebar
        self.sidebarWidget = QWidget()
        self.sidebar_layout = QVBoxLayout(self.sidebarWidget)

        self.masterLayout.addWidget(self.titlebar)

        # creating view stack
        self.view_stack = QStackedWidget()
        self.masterLayout.addWidget(self.view_stack, stretch=1)

        # creating the basic calculator
        self.basic_calculator = basic()
        # adding the basic calculator to the stack
        self.view_stack.addWidget(self.basic_calculator)

        # loading the stylesheet
        self.loadStylesheet()

    """ 
    Reads the external QSS file and applies it globally to the window.
    """

    def loadStylesheet(self):
        try:
            with open("gui/style.css", "r") as f:
                style_data = f.read()
                self.setStyleSheet(style_data)
        except FileNotFoundError:
            print("Warning: style.qss not found. Running with default system theme.")

    """
    Toggles the maximized state of the window.
    """

    def toggleMaximize(self):
        if self.isMaximized():
            self.showNormal()
            self.btn_maximize.setText("🗖")
        else:
            self.showMaximized()
            self.btn_maximize.setText("🗗")

    """
    Window dragging Functions
    """

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and self.titlebar.underMouse():
            self.drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self.titlebar.underMouse():
            self.move(event.globalPosition().toPoint() - self.drag_position)
            event.accept()
