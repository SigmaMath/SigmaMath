from PySide6.QtWidgets import QPushButton, QSizePolicy

""" Imported classes from PySide6
    QPushButton: Button Class
"""

""" Custom Buttons Class
    For better control and knowledge of the buttons
    It inherits from QPushButton
    type element holds the nature of the button
    styleClass property added to object for custom styling
"""


class button(QPushButton):
    def __init__(self, text, type="number"):
        super().__init__(text)
        # self.setFixedHeight(50)
        self.type = type
        self.setProperty("styleClass", self.type)
        
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
