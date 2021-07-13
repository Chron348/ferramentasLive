from PySide6.QtWidgets import QWidget


class QtssFormatter():
    @staticmethod
    def importFile(file_path: str, qwidget: QWidget):
        cssFormater = ''
        file = open(file_path)
        for line in file.readlines():
            cssFormater += line
        qwidget.setStyleSheet(cssFormater)
