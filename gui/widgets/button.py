import io
import matplotlib as mpl
import matplotlib.pyplot as plt
from PySide6.QtWidgets import QPushButton, QSizePolicy
from PySide6.QtGui import QPixmap, QIcon

""" Imported Libraries
    PySide6: PySide6 Library
    matplotlib: Matplotlib Library
    io: IO Library
"""

""" Imported classes from PySide6
    QPushButton: Button Class
    QSizePolicy: Size Policy Class
    QLabel: Label Class
    QVBoxLayout: Vertical Layout Class
    Qt: Qt Class
    QPixmap: Image Class
    QIcon: Icon Class
"""

""" Custom Buttons Class
    For better control and knowledge of the buttons
    It inherits from QPushButton
    btn_type element holds the nature of the button
    styleClass property added to object for custom styling
"""

mpl.rcParams["mathtext.fontset"] = "stix"  # use stix font for math
mpl.rcParams["font.family"] = "STIXGeneral"  # use stix font for text


class button(QPushButton):
    def __init__(self, text, btn_type="number", ltx_tk=None):
        super().__init__()
        self.setMinimumHeight(60)
        self.btn_type = btn_type
        self.setProperty("styleClass", self.btn_type)

        # handeling ltx_tk if passed else use text for the output string
        self.ltx_tk = ltx_tk if ltx_tk is not None else text

        # Expanding the size policy so that the button can be resized without issues
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        """ text handeling for the button will be based on the wheter the passed
            text is simple sting or a ltx_tk expression"""

        if text.startswith("$") and text.endswith("$"):  # ltx_tk expression
            self.addLatex(text)
        else:
            self.setText(text)

    """ the method for handeling ltx_tk expression
        it converts strings into vectors
    """

    def addLatex(self, text):
        buf = io.BytesIO()  # create a buffer for image in ram
        dpi = 200
        fig, ax = plt.subplots(
            figsize=(60 / dpi, 1), dpi=200
        )  # create a figure and axis with high dpi
        fig.patch.set_facecolor("none")  # transparent background
        ax.axis("off")  # hide axis

        ax.text(
            0.5,
            0.5,
            text,
            size=12,
            color="white",
            horizontalalignment="center",
            verticalalignment="center",
            linespacing=0.1,
        )  # text properties

        plt.savefig(
            buf, format="png", bbox_inches="tight", pad_inches=0.0, transparent=True
        )  # save figure to buffer
        plt.close(fig)  # close figure
        buf.seek(0)  # seek to the beginning of the buffer

        pixmap = QPixmap()  # create a pixmap
        pixmap.loadFromData(buf.getvalue())  # load image from buffer

        self.setIcon(QIcon(pixmap))
        self.setIconSize(pixmap.size() / 2)