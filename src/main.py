#!/usr/bin/python3

import os
import sys

from PyQt5 import uic
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow, QSystemTrayIcon, QDialog, QStyle, QMenu
from PyQt5.QtGui import QIcon

GUI_FOLDER = './gui/'  # Where the .ui files are saved


class TrayIcon(QSystemTrayIcon):
    def __init__(self, icon, parent=None):
        QSystemTrayIcon.__init__(self, icon, parent)
        self.menu = QMenu(parent)
        self.configAction = self.menu.addAction("Configuration")
        self.encryptAction = self.menu.addAction("Encrypt")
        self.decryptAction = self.menu.addAction("Decrypt")
        self.exitAction = self.menu.addAction("Exit")
        self.setContextMenu(self.menu)
        # Load Window
        self.encryptWin = Encrypt()
        self.configDialog = Config()
        # Using the signal
        self.configAction.triggered.connect(self.config)
        self.encryptAction.triggered.connect(self.encrypt)
        self.decryptAction.triggered.connect(self.decrypt)
        self.exitAction.triggered.connect(self.kill)

    @pyqtSlot()
    def config(self):
        self.configDialog.show()

    def encrypt(self):
        self.encryptWin.show()

    def decrypt(self):
        pass

    def kill(self):
       sys.exit(app.exec_())

class Encrypt(QMainWindow):
    def __init__(self):
        # We need this to load the GUI
        super(Encrypt, self).__init__()
        uic.loadUi(GUI_FOLDER + 'main.ui', self)
        self.encryptBtn.setDisabled(True)
        # Signals
        self.folderBtn.clicked.connect(self.pickFolder)
        self.fileView.itemClicked.connect(self.pickFile)

    @pyqtSlot()
    def pickFolder(self):
        folder = QFileDialog.getExistingDirectory()
        if(folder != ''):
            self.folder = folder
            self.refresh()
        else:
            self.encryptBtn.setDisabled(True)

    def refresh(self):
        self.fileView.clear()
        for i in sorted(os.listdir(self.folder)):
            path = os.path.join(self.folder, i)
            if not (os.path.isdir(path)):
                self.fileView.addItem(i)

    def pickFile(self):
        self.encryptBtn.setDisabled(False)

class Config(QDialog):
    def __init__(self):
        # We need this to load the GUI
        super(Config, self).__init__()
        uic.loadUi(GUI_FOLDER + 'config.ui', self)
        self.desRadio.setChecked(True)
        self.gdRadio.setChecked(True)
        self.gzRadio.setChecked(True)
        self.folderLn.setText('/home/mrat/Hx2017/Desencriptada/')
        # Signals
        self.openBtn.clicked.connect(self.openFold)

    @pyqtSlot()
    def openFold(self):
        line = QFileDialog.getExistingDirectory()
        if line != '':
            self.folderLn.setText(line)

# main function
def main():
    app = QApplication(sys.argv)
    style = app.style()
    icon = QIcon(style.standardPixmap(QStyle.SP_FileIcon))
    trayIcon = TrayIcon(icon)
    trayIcon.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
