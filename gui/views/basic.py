from PySide6.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QLineEdit, QSizePolicy
from PySide6.QtCore import Qt
from core import Engine
from gui.widgets.button import button
from gui.widgets.screen import screen

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

        # creating an instance of the engine
        self.engine = Engine()

        # creating the vertical stack layout which is bound to the basic class object
        self.stack = QVBoxLayout(self)
        self.stack.setContentsMargins(5, 5, 5, 5)  # adding margins to the layout

        # # creating the screen for input
        # self.screen_in = screen()
        # self.screen_in.setObjectName("screen_in")
        # self.screen_in.setPlaceholderText(None)  # setting the placeholder text
        # self.screen_in.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        # self.screen_in.setMinimumHeight(50)
        # self.screen_in.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # self.stack.addWidget(self.screen_in, stretch=1)  # adding the screen_out to the layout

        # # creating the screen for output
        # self.screen_out = screen()
        # self.screen_out.setPlaceholderText("0")  # setting the placeholder text
        # self.screen_out.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        # self.screen_out.setMinimumHeight(100)
        # self.screen_out.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # self.stack.addWidget(self.screen_out, stretch=2)  # adding the screen_out to the layout
        # self.screen_out.setReadOnly(True)

        # creating the button grid
        self.button_grid = QGridLayout()
        # adding the button grid to the layout
        self.stack.addLayout(self.button_grid, stretch=6)
        self.button_grid.setSpacing(2)  # setting the spacing

        # Define the visual arrangement of your keypad matrix: (Text, StyleClass)
        button_matrix = [
            [
                ("%", "operator", r"\div 100"),
                (r"$x^2$", "operator", "^2"),
                (r"$1/x$", "operator", "1/"),
                (r"$^{\!2\!}\sqrt{x}$", "operator", r"\sqrt{"),
            ],
            [
                ("(", "operator"),
                (")", "operator"),
                ("Del", "utility", "del"),
                ("÷", "operator", r"\div"),
            ],
            [("7", "number"), ("8", "number"), ("9", "number"), ("×", "operator", r"\times")],
            [("4", "number"), ("5", "number"), ("6", "number"), ("-", "operator")],
            [("1", "number"), ("2", "number"), ("3", "number"), ("+", "operator")],
            [
                ("0", "number"),
                (".", "number"),
                ("C", "utility", "clear"),
                ("=", "operator", "equal"),
            ],
        ]

        # Loop through rows and columns to spawn instances dynamically
        for row, element in enumerate(button_matrix):
            for col, tuple in enumerate(element):

                text = tuple[0]
                btn_type = tuple[1]
                ltx_tk = tuple[2] if len(tuple) > 2 else None

                # Instance of custom button class from your widgets file
                btn = button(text, btn_type=btn_type, ltx_tk=ltx_tk)

                """ Temporary Lambda Function:
                    Creates a unique function instance for this specific button,
                    using a default argument (b=btn) to freeze its current identity 
                    in memory before the loop moves on.
                """
                btn.clicked.connect(lambda checked=False, b=btn: self.onPress(b))

                # QGridLayout using its specific coordinate indexes
                self.button_grid.addWidget(btn, row, col)

    # def onPress(self, btn):
    #     token = btn.ltx_tk if btn.ltx_tk is not None else btn.text()
    #     text = self.screen_in.text()
    #     pos = self.screen_in.cursorPosition()

    #     if token == "clear":
    #         self.screen_in.clear()
    #         self.screen_out.clear()
    #         self.screen_out.update("")
    #         return

    #     elif token == "del":
    #         if pos == 0:
    #             return

    #         new_text = text[:pos - 1] + text[pos:]
    #         self.screen_in.overlay.setText(new_text)
    #         self.screen_in.setCursorPosition(pos - 1)
    #         self.screen_in.update(new_text)
    #         return

    #     elif token == "equal":
    #         return

    #     else:
    #         new_text = text[:pos] + token + text[pos:]
    #         self.screen_in.overlay.setText(new_text)
    #         self.screen_in.setCursorPosition(pos + len(token))
    #         self.screen_in.update(new_text)
    #         return
