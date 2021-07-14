from UI.hfWidget import HFWidget
from PySide6 import QtWidgets
import sys

import io

from PySide6.QtGui import QColor, QPalette

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    hf = HFWidget()

    # estilizando uma janela com a funcao built-in
    # window2 = QtWidgets.QMainWindow()
    # window2.resize(400,400)
    # layout = window2.layout()
    # layout.addWidget(QtWidgets.QPushButton("Push"))
    # QtssFormatter.importFile("livetools/style.qtss", window2)
    # window2.show()

    # mdi example
    # window2 = QtWidgets.QMdiSubWindow(hf)
    # window2.resize(400,400)
    # window2.show()

    sys.exit(app.exec())
