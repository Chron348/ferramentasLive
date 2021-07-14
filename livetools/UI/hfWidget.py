from PySide6.QtWidgets import QMainWindow, QTextEdit, QComboBox, QLabel
from livetools.services.remoteConnection import RemoteConnection

class HFWidget(QMainWindow):
    def __init__(self) -> None:
        super(HFWidget, self).__init__()
        self.initWidgets()
        self.resize(800, 400)
        self.show()

    def initWidgets(self):

        self.combo_liveVersions = QComboBox()

        versoesLiveServer = RemoteConnection().list_folder_server_live_remote_windows_host()
        versoesLiveServer.insert(0, '-- Versões Live Server --')

        self.label_liveVersions = QLabel()
        self.label_liveVersions.setText('Versões Live Server')

        self.combo_liveVersions.addItems(versoesLiveServer)
        self.combo_liveVersions.setMaximumWidth(200)
        self.combo_liveVersions.setFixedHeight(26)

        self.textLiveVersion = QTextEdit()
        self.textLiveVersion.setFixedHeight(26)
        layout = self.layout()

        layout.addWidget(self.textLiveVersion)
        layout.addWidget(self.combo_liveVersions)

