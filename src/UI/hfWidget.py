from PySide6.QtCore import QSize
from PySide6.QtGui import QScreen, QWindow
from PySide6.QtWidgets import QMainWindow, QTextEdit


class HFWidget(QMainWindow):
    def __init__(self) -> None:
        super(HFWidget, self).__init__()
        self.initWidgets()
        self.resize(800, 400)
        self.show()

    def initWidgets(self):

        self.textLiveVersion = QTextEdit()
        self.textLiveVersion.setFixedHeight(26)
        layout = self.layout()

        

        layout.addWidget(self.textLiveVersion)

