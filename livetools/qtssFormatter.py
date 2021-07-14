from PySide6.QtWidgets import QWidget


class QtssFormatter():

    def __init__(self):
        pass

    @staticmethod
    def import_file(file_path: str, qwidget: QWidget):
        css_formatter = ''
        file = open(file_path)
        for line in file.readlines():
            css_formatter += line
        qwidget.setStyleSheet(css_formatter)
