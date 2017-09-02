#!/usr/bin/python3

import os
import sys

from PyQt5 import uic
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow

GUI_FOLDER = './gui/'  # Where the .ui files are saved


class MainWindow(QMainWindow):
    def __init__(self):
        # We need this to load the GUI
        super(MainWindow, self).__init__()
        uic.loadUi(GUI_FOLDER + 'main.ui', self)
        # We'll set text
        self.ftpRadio.setText('FTP')
        self.gdRadio.setText('Google Drive')
        self.dropboxRadio.setText('Dropbox')
        self.odRadio.setText('One Drive')
        self.connectBtn.setText('Connect')
        self.configBtn.setText('Configurate')

# main function
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
