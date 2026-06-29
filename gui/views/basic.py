from PySide6.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QLineEdit
from PySide6.QtCore import Qt
from gui.widgets import button

""" Imported libraries
    PySide6: PySide6 Library
    custom widgets {file location : gui/widgets.py} contains custom widgets class
"""

""" Imported classes from PySide6
    QWidget: Widget Class
    QVBoxLayout: Vertical Layout Class
    QGridLayout: Grid Layout Class
    QLineEdit: Line Edit Class
    Qt: Qt Class
"""

""" Imported Class from gui.widgets.py
    button: Custom Button Class
"""


class basic(QWidget):
    def __init__(self):
        super().__init__()

        # creating the vertical stack layout which is bound to the basic class object
        self.stack = QVBoxLayout(self)
        self.stack.setContentsMargins(5, 5, 5, 5)  # adding margins to the layout

        # creating the screen
        self.screen = QLineEdit()
        self.screen.setPlaceholderText("0")  # setting the placeholder text
        self.screen.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.screen.setMinimumHeight(200)
        self.stack.addWidget(self.screen, stretch=1)  # adding the screen to the layout

        # creating the button grid
        self.button_grid = QGridLayout()
        # adding the button grid to the layout
        self.stack.addLayout(self.button_grid, stretch=3)
        self.button_grid.setSpacing(2)  # setting the spacing

        # Define the visual arrangement of your keypad matrix: (Text, StyleClass)
        button_matrix = [
            [
                ("%", "operator"),
                (r"$x^2$", "operator"),
                (r"$1/x$", "operator"),
                (r"$^{\!2\!}\sqrt{x}$", "operator"),
            ],
            [
                ("(", "utility"),
                (")", "utility"),
                ("Del", "utility"),
                ("÷", "operator"),
            ],
            [("7", "number"), ("8", "number"), ("9", "number"), ("×", "operator")],
            [("4", "number"), ("5", "number"), ("6", "number"), ("-", "operator")],
            [("1", "number"), ("2", "number"), ("3", "number"), ("+", "operator")],
            [("0", "number"), (".", "number"), ("C", "utility"), ("=", "operator")],
        ]

        # Loop through rows and columns to spawn instances dynamically
        for row, element in enumerate(button_matrix):
            for col, (text, btn_type) in enumerate(element):

                # 1. Instantiate your custom button class from your widgets file
                btn = button(text, btn_type=btn_type)

                # 2. Add it to your QGridLayout using its specific coordinate indexes
                self.button_grid.addWidget(btn, row, col)
