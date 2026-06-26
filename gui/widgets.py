from PySide6.QtWidgets import QPushButton, QSizePolicy

""" Imported classes from PySide6
    QPushButton: Button Class
"""

""" Custom Buttons Class
    For better control and knowledge of the buttons
    It inherits from QPushButton
    btn_type element holds the nature of the button
    styleClass property added to object for custom styling
"""


class button(QPushButton):
    def __init__(self, text, btn_type="number"):
        super().__init__(text)
        # self.setFixedHeight(50)
        self.btn_type = btn_type
        self.setProperty("styleClass", self.btn_type)

        # Expanding the size policy so that the button can be resized without issues
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
